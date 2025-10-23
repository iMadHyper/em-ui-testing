import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope='session')
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope='class')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()