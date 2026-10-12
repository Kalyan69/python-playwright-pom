import json
from pathlib import Path

from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.navigation_page import NavigationPage


TEST_DATA_PATH = Path(__file__).parents[1] / "test_data" / "test_data.json"
with TEST_DATA_PATH.open(encoding="utf-8") as test_data_file:
    TEST_DATA = json.load(test_data_file)


def test_verified_software_testing_types_link_navigates(
    configured_page: Page,
) -> None:
    home_page = HomePage(configured_page)
    navigation_page = NavigationPage(configured_page)

    home_page.open_home_page()
    article_page = navigation_page.open_software_testing_types(
        TEST_DATA["verified_navigation_link"]
    )

    expect(article_page).to_have_url(
        navigation_page.software_testing_types_url()
    )
    expect(article_page).to_have_title(
        TEST_DATA["software_testing_types_title"]
    )
