
from playwright.sync_api import Page, expect

def test_keyboard_ops(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    ipbox1= page.locator("#input1")
    ipbox2 = page.locator("#input2")
    ipbox3 = page.locator("#input3")
    ipbox1.focus()
    page.keyboard.insert_text("welcome")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    expect(ipbox2).to_have_value("welcome")
    expect(ipbox3).to_have_value("welcome")
