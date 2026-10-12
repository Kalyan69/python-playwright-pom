from playwright.sync_api import Page


class BasePage:
    """Shared browser actions used by page objects."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open_url(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def get_page_title(self) -> str:
        return self.page.title()

    def wait_for_page_load(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")
