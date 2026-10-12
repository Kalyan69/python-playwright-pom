import re

from playwright.sync_api import Locator, expect

from pages.base_page import BasePage
from utils.config import BASE_URL


class HomePage(BasePage):
    """Interactions and checks for the QAFox homepage."""

    @property
    def logo(self) -> Locator:
        return self.page.get_by_role("link", name="QAFox", exact=True)

    @property
    def courses_navigation_link(self) -> Locator:
        return self.page.get_by_role("link", name=re.compile(r"^Courses"))

    def primary_content_heading(self, heading: str) -> Locator:
        return self.page.get_by_role(
            "heading", name=heading, exact=True
        )

    def open_home_page(self) -> None:
        self.open_url(BASE_URL)

    def verify_home_page_loaded(self) -> None:
        expect(self.logo).to_be_visible()

    def verify_home_page_title(self, expected_title: str) -> None:
        expect(self.page).to_have_title(expected_title)

    def verify_main_navigation_visible(self) -> None:
        expect(self.courses_navigation_link).to_be_visible()

    def verify_primary_content_visible(self, heading: str) -> None:
        expect(self.primary_content_heading(heading)).to_be_visible()

    def verify_home_page_url(self) -> None:
        expected_url = re.compile(rf"^{re.escape(BASE_URL.rstrip('/'))}/?$")
        expect(self.page).to_have_url(expected_url)
