import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from testcontr.datacontr import *
from testcontr.locatorscontr import *


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture
def login(page: Page):
    def login_function():
        page.goto(data_web_adress_herokuapp)
        page.fill(locator_field_user_name, data_username)
        page.fill(locator_field_user_pass, data_password)
        page.click(locator_button_login)
        page.screenshot(path=f"screenshotcontr/login.png")
    return login_function

@pytest.fixture
def logout(page: Page):
    def logout_function():
        page.goto(data_web_adress_herokuapp)
        page.fill(locator_field_user_name, data_username)
        page.fill(locator_field_user_pass, data_password)
        page.click(locator_button_login)
        page.click(locator_button_logout)
        page.wait_for_timeout(1000)
        page.screenshot(path=f"screenshotcontr/logout.png")
    return logout_function
