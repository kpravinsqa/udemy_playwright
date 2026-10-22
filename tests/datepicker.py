from playwright.sync_api import Page, expect


def test_jquery_datepicker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    datepicker = page.locator("#datepicker")
    datepicker.fill("10/20/2026")
    expect(datepicker).to_have_value("10/20/2026")

def test_dddatepicker(page:Page,):
    page.goto("https://testautomationpractice.blogspot.com/")
    dddatepicker= page.locator("#txtDate").click()
    monthdd = page.locator(".ui-datepicker-month")
    monthdd.select_option("Nov")
    yeardd = page.locator(".ui-datepicker-year")
    yeardd.select_option("2025")
    dates = page.locator("table[class='ui-datepicker-calendar'] tbody tr td").all()
    for date in dates:
        if date.inner_text() == "23":
            date.click()
            break

def dob(targetday, targetmonth, targetyear, is_future, page: Page):

    while True:
        current_month = page.locator(".ui-datepicker-month").inner_text()
        current_year = page.locator(".ui-datepicker-year").inner_text()
        print(f"Current Month: {current_month}, Current Year: {current_year}")
        # if current_month == targetmonth and current_year == targetyear:
        #     break
        # if is_future==True:
        #     page.locator(".ui-icon.ui-icon-circle-triangle-e").click()
        # else:
        #     page.wait_for_timeout(3000)
        #     page.locator(".ui-icon.ui-icon-circle-triangle-w").click()
        # dates = page.locator("table[class='ui-datepicker-calendar'] tbody tr td").all()
        # for date in dates:
        #     if date.inner_text() == targetday:
        #         date.click()
        #         break

dob("16", "Mar", "1995", False, Page)

def test_dummyticket(page:Page):
    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    page.locator("#product_549").click()
    page.locator("#travname").fill("Pravin")
    page.locator("#travlastname").fill("Khedkar")
    dobbox = page.locator("#dob")
    dobbox.click()
    dob("16","Mar","1995",False,page)
    expect(dobbox).to_have_value("16/03/1995")





