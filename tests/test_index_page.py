import pytest
import pages
from pages.index_page import IndexPage


class TestFooter:
    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        ind_pg = IndexPage()
        ind_pg.open_index_page(page)
        actual_result = ind_pg.get_text_from_google_search_button(page)
        assert actual_result == 'Google Search', 'Google Search button text is not correct'


