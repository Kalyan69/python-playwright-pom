from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """Search actions and result checks for QAFox."""

    @property
    def search_box(self) -> Locator:
        return self.page.get_by_role("searchbox", name="Search for...")

    def search_for(self, search_term: str) -> None:
        self.search_box.fill(search_term)
        self.search_box.press("Enter")

    def verify_search_term(self, search_term: str) -> None:
        expect(
            self.page.get_by_role(
                "heading",
                name=f"Search Results for: {search_term}",
                exact=True,
            )
        ).to_be_visible()

    def verify_result_visible(self, result_title: str) -> None:
        results = self.page.get_by_role("main").get_by_role(
            "heading", name=result_title, level=2, exact=True
        )
        expect(results).to_be_visible()
