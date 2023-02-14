import pytest
from playwright.sync_api import Playwright, sync_playwright
from pages.login_page import LoginPage


def test_valid_login(playwright: Playwright):
    # Start a new browser context
    with playwright.chromium.launch() as browser:
        with browser.new_context() as context:
            # Create a LoginPage object and navigate to the login page
            page = context.new_page()
            login_page = LoginPage(page)
            login_page.goto()

            # Log in with valid credentials
            login_page.login("standard_user", "secret_sauce")

            # Check that the inventory page is loaded
            assert login_page.is_login_successful()

            # Perform additional tests on the inventory page here