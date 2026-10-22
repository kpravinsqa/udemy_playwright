
# from playwright.sync_api import Page, expect
#
# def test_autosuggestive_dd(page:Page):
#     page.goto("https://www.flipkart.com/")
#     page.wait_for_timeout(3000)
#     page.locator(".b3wTlE").click()
#     page.wait_for_timeout(3000)
#     textbox= page.locator(".nw1UBF.v1zwn26").nth(1).fill("smart")
#     results = page.locator(".wT2Zoz")
#     for result in results.all_inner_texts():
#         print(result)
#     for result in results.all_inner_texts():
#         if "smartphone" in result.lower():
#             result.click()
#             break
#     expect(textbox).to_have_value("smartphone")

#claude :
import re
from playwright.sync_api import Page, expect


def test_autosuggestive_dd(page: Page):
    page.goto("https://www.flipkart.com/")

    # Close login popup if it appears (don't fail if it doesn't)
    close_btn = page.locator("span[role='button']:has-text('✕')")
    if close_btn.is_visible():
        close_btn.click()

    # Target the visible, editable search box, not the hidden/readonly copies
    search = page.locator("input[name='q']:visible").first
    search.click()  # some layouts swap a readonly box for the real one on click
    textbox = page.locator("input[name='q']:not([readonly]):visible").first
    textbox.fill("smart")

    # Wait for suggestions to actually appear
    results = page.locator(".wT2Zoz")
    results.first.wait_for(state="visible")

    for text in results.all_inner_texts():
        print(text)

    # Iterate Locators (clickable), not strings
    for result in results.all():
        if "smartphone" in result.inner_text().lower():
            result.click()
            break
    else:
        raise AssertionError("No 'smartphone' suggestion found")

    # Assert on navigation + input value
    expect(page).to_have_url(re.compile(r"q=smartphone", re.I))
    expect(page.locator("input[name='q']:visible").first).to_have_value(
        re.compile("smartphone", re.I)
    )
