import pytest
from playwright.sync_api import Playwright, sync_playwright

def test_valid_login(playwright: Playwright):
    with playwright.chromium.launch(headless=True) as browser:
        with browser.new_context() as context:
            # Go to login page
            page = context.new_page()
            page.goto('https://www.saucedemo.com/')

            # Login
            page.fill('#user-name', 'standard_user')
            page.fill('#password', 'secret_sauce')
            page.click('#login-button')

            # Verify that we are logged in and redirected to the inventory page
            assert 'inventory' in page.url