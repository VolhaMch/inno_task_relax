import os

import allure
import pytest
from playwright.sync_api import sync_playwright

from pages.base_page import BasePage
from utils.config import BASE_URL


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    headless_mode = os.getenv("HEADLESS", "true").lower() == "false"
    browser = playwright_instance.chromium.launch(headless=headless_mode)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def open_main_page(page):
    base_page = BasePage(page)
    with allure.step("Open the main page"):
        base_page.open_page(BASE_URL)
    with allure.step("Accept cookies"):
        base_page.accept_cookies()
    return base_page