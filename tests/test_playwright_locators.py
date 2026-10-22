from playwright.sync_api import Playwright, expect, Page
import pytest
import re

url = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"
def test_get_by_role(page:Page):
    page.goto(url)
    button = page.get_by_role("button", name="Primary Action")
    expect(button).to_be_visible()

def test_get_by_text(page:Page):
    page.goto(url)
    button = page.get_by_text("Submit Form")
    expect(button).to_be_enabled()

def test_get_by_label(page:Page):
    page.goto(url)
    expect(page.get_by_label("Email Address:")).to_be_visible()

def test_get_by_placeholder(page:Page):
    page.goto(url)
    expect(page.get_by_placeholder("Enter your full name")).to_be_visible()

def test_alt_text(page:Page):
    page.goto(url)
    expect(page.get_by_alt_text("logo image")).to_be_visible()

def test_title(page:Page):
    page.goto(url)
    expect(page.get_by_title("Home page link")).to_be_visible()

def test_testid(page:Page):
    page.goto(url)
    expect(page.get_by_test_id("edit-profile-btn")).to_be_visible()

