from playwright.sync_api import Page
import config
from config.url import Url


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnk']"
    _LINK_ENGLISH_LANG = "//a[contains(text(), 'English')]"

    def open_index_page(self, page: Page) -> None:
        link = Url()
        page.goto(link.DOMAIN)

    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_ENGLISH_LANG).click()

    def get_text_from_google_search_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_GOOGLE_SEARCH).text_content()



