
from playwright.sync_api import Playwright, expect


def test_handlepoups(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("popup", lambda popup: popup.wait_for_load_state() )
    page.locator("#PopUp").click()

    all_popups =  context.pages

    for popup in all_popups:
        print(popup.title())
        if popup.title() == "Selenium":
            expect(popup.locator('.d-1.fw-bold')).to_have_text("Selenium automates browsers. That's it!")


