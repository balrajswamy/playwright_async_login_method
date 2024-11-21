import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        email = "admin@gmail.com"
        pwd = "admin@123"
        page.goto("https://app.vwo.com/#/login")
        page.fill("input[name='username']", email)
        page.fill("input[name='password']", pwd)
        page.get_by_role("button", name="Sign in", exact=True).click()
        page.wait_for_timeout(2000)
        #error_message = page.get_by_text("Your email, password, IP").click()
        page.wait_for_selector('#js-notification-box-msg')

        notification_text = page.locator("#js-notification-box-msg").text_content()
        assert "Your email" in notification_text, "Not reached the error notification"

        # ---------------------
        context.close()
        browser.close()



