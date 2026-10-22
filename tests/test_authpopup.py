from playwright.sync_api import Playwright,expect, Page

def test_urlauthpopup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    expect(page.locator('.example')).to_be_visible()

def test_context(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context(http_credentials={'username':'admin','password':'admin'})
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(page.locator('.example')).to_be_visible()

