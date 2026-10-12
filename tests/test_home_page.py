import json
from pathlib import Path

from playwright.sync_api import Page

from pages.home_page import HomePage


TEST_DATA_PATH = Path(__file__).parents[1] / "test_data" / "test_data.json"
with TEST_DATA_PATH.open(encoding="utf-8") as test_data_file:
    TEST_DATA = json.load(test_data_file)


def test_tc001_homepage_opens_successfully(configured_page: Page) -> None:
    home_page = HomePage(configured_page)
    home_page.open_home_page()

    home_page.verify_home_page_loaded()


def test_tc002_homepage_title_is_correct(configured_page: Page) -> None:
    home_page = HomePage(configured_page)
    home_page.open_home_page()

    home_page.verify_home_page_title(TEST_DATA["home_page_title"])


def test_tc003_main_navigation_is_visible(configured_page: Page) -> None:
    home_page = HomePage(configured_page)
    home_page.open_home_page()

    home_page.verify_main_navigation_visible()


def test_tc004_expected_primary_content_is_visible(configured_page: Page) -> None:
    home_page = HomePage(configured_page)
    home_page.open_home_page()

    home_page.verify_primary_content_visible(
        TEST_DATA["primary_content_heading"]
    )


def test_tc005_homepage_url_is_correct(configured_page: Page) -> None:
    home_page = HomePage(configured_page)
    home_page.open_home_page()

    home_page.verify_home_page_url()
