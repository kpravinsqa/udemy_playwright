from playwright.sync_api import Page, expect, sync_playwright


def test_ipbox(page:Page, base_url):
    page.goto(base_url)
    name = page.locator("#name").fill("Pravin")
    email = page.locator(".form-control").nth(1).fill("pbk@123.com")
    phone = page.get_by_placeholder("Enter Phone").fill("1234567890")
    address = page.get_by_label("Address:").fill("Pune")

    expect(name).to_have_value("Pravin")
    expect(email).to_have_value("pbk@123.com")
    expect(phone).to_have_value("1234567890")
    expect(address).to_have_value("Pune")

def test_rdbutton(page:Page, base_url):
    page.goto(base_url)
    page.locator("input[name='gender']").nth(0).check()
    expect(page.locator("input[name='gender']").nth(0)).to_be_checked()
    page.locator("input[name='gender']").nth(1).check()
    expect(page.locator("input[name='gender']").nth(1)).to_be_checked()

def test_checkboxes(page:Page, base_url):
    page.goto(base_url)
    chkbox = page.locator(".form-check-input").all()
    weekdays = chkbox[2:]

    for day in weekdays:
        day.check()
        expect(day).to_be_checked()


