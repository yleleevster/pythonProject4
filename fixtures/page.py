import pytest
import config
from config.expectations import Expectations
from config.playwright import Playwright
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


@pytest.fixture()
def page() -> Page:
    plw = Playwright()
    playwright = sync_playwright().start()
    if plw.BROWSER == 'firefox':
        browser = get_firefox_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    elif plw.BROWSER == 'chrome':
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


def get_firefox_browser(playwright) -> Browser:
    plw = Playwright()
    return playwright.firefox.launch(
        headless=plw.IS_HEADLESS,
        slow_mo=plw.SLOW_MO,
    )


def get_chrome_browser(playwright) -> Browser:
    plw = Playwright()
    return playwright.chromium.launch(
        headless=plw.IS_HEADLESS,
        slow_mo=plw.SLOW_MO
    )


def get_context(browser) -> BrowserContext:
    plw = Playwright()
    exp = Expectations()
    context = browser.new_context(
        viewport=plw.PAGE_VIEWPORT_SIZE,
        locale=plw.LOCALE
    )
    context.set_default_timeout(
        timeout=exp.DEFAULT_TIMEOUT
    )
    return context