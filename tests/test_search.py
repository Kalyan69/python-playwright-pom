import json
from pathlib import Path

import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


TEST_DATA_PATH = Path(__file__).parents[1] / "test_data" / "test_data.json"
with TEST_DATA_PATH.open(encoding="utf-8") as test_data_file:
    TEST_DATA = json.load(test_data_file)


@pytest.mark.parametrize(
    "search_case",
    TEST_DATA["search_cases"],
    ids=lambda search_case: search_case["term"],
)
def test_search_returns_expected_result(
    configured_page: Page, search_case: dict[str, str]
) -> None:
    home_page = HomePage(configured_page)
    search_results_page = SearchResultsPage(configured_page)

    home_page.open_home_page()
    search_results_page.search_for(search_case["term"])
    search_results_page.verify_search_term(search_case["term"])
    search_results_page.verify_result_visible(search_case["expected_result"])
