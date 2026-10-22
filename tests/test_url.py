from playwright.sync_api import Page, expect
import pytest

def test_url(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    print(page.url)
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/")

def test_title(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    print(page.title())
    expect(page).to_have_title("Test Automation Practice")