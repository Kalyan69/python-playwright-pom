from datetime import datetime
from pathlib import Path
import re
from collections.abc import Generator

import pytest
from playwright.sync_api import Page

from utils.config import DEFAULT_TIMEOUT_MS


SCREENSHOT_DIR = Path(__file__).with_name("screenshots")
_reports_key = pytest.StashKey[list[pytest.TestReport]]()


@pytest.fixture
def configured_page(page: Page) -> Page:
    """Apply the framework timeout to pytest-playwright's managed page."""
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item,
) -> Generator[None, None, None]:
    outcome = yield
    report = outcome.get_result()
    reports = item.stash.get(_reports_key, [])
    reports.append(report)
    item.stash[_reports_key] = reports

    if report.when == "call" and report.failed:
        page = item.funcargs.get("configured_page")
        if isinstance(page, Page):
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            safe_test_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
            screenshot_path = SCREENSHOT_DIR / f"{safe_test_name}-{timestamp}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            report.sections.append(("Failure screenshot", str(screenshot_path)))
