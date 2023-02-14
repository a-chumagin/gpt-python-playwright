from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def is_login_successful(self):
        return self.page.url == "https://www.saucedemo.com/inventory.html"
