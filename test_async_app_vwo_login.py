from jinja2.async_utils import auto_await
from playwright.async_api import async_playwright
import asyncio
import pytest

@pytest.mark.asyncio
async def test_app_login():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False,slow_mo=1000)
        context1 = await browser.new_context()
        page = await context1.new_page()

        email = "admin@gmail.com"
        pwd = "admin@123"

        await page.goto("https://app.vwo.com/#/login")
        print("title=>",await page.title())
        await page.fill("input[name='username']", email)
        await page.fill("input[name='password']", pwd)
        try:
            #await page.click("text=Sign in")
            await page.click('//button//span[text()="Sign in"]')

            await page.screenshot(path="src/tests/ex_21112024/example.png")

            print("done")
        except:
            await page.click("button[type='submit']")
        await page.wait_for_timeout(2000)
        await page.wait_for_selector('#js-notification-box-msg')

        notification_text = await page.locator("#js-notification-box-msg").text_content()

        # Print the extracted text
        print(f"Notification Text: {notification_text}")

        # Assert the content (optional)
        expected_text = "Your email, password, IP address or location did not match"
        assert notification_text.strip() == expected_text, "Notification text did not match!"

        # Check for success or error
        if await page.is_visible("div.dashboard"):
            print(f"Login successful for user: {email}")
        else:
            print(f"Login failed for user: {email}")
        # Close browser
        await browser.close()


#asyncio.run(test_app_login())