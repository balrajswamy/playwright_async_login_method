import asyncio
from playwright.async_api import async_playwright

async def test_vwo_login():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # Open new page
        page = await context.new_page()

        # Navigate to the URL
        await page.goto("https://app.vwo.com/#/login")

        # Verify the page title
        title = await page.title()
        assert title == "Login - VWO", f"Expected title to be 'Login - VWO', but got '{title}'"

        # Verify the presence of login form fields
        assert await page.is_visible("input[name='email']"), "Email input field is not visible"
        assert await page.is_visible("input[name='password']"), "Password input field is not visible"
        assert await page.is_visible("button[type='submit']"), "Login button is not visible"

        # Optionally, you can fill in the login form for further testing
        await page.fill("input[name='email']", "test@example.com")
        await page.fill("input[name='password']", "password123")
        await page.click("button[type='submit']")

        # Add an assertion or validation after submitting the form
        # For example: Validate error messages or redirection

        # Close browser
        await browser.close()

# Run the test
asyncio.run(test_vwo_login())
