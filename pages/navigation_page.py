from playwright.sync_api import Page

from pages.base_page import BasePage
from utils.config import BASE_URL


class NavigationPage(BasePage):
    """Interactions for verified internal links on QAFox."""

    def open_software_testing_types(self, link_name: str) -> Page:
        link = self.page.get_by_role(
            "link", name=link_name, exact=True
        )
        with self.page.expect_popup() as popup_info:
            link.click()
        article_page = popup_info.value
        article_page.wait_for_load_state("domcontentloaded")
        return article_page

    @staticmethod
    def software_testing_types_url() -> str:
        return f"{BASE_URL.rstrip('/')}/170-plus-software-testing-types/"
