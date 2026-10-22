from playwright.sync_api import Page, expect


def test_dd(page:Page):
    page.goto("https://bstackdemo.com/")
    page.wait_for_load_state()
    optiondd = page.get_by_role("combobox")
    expect(optiondd).to_be_visible()
    expect(optiondd).to_be_enabled()
    optiondd.select_option("Lowest to highest")
    page.wait_for_timeout(3000)
    product_names = page.locator("shelf-item__title").all_inner_texts()
    product_prices = page.locator("div[class='val'] b").all_inner_texts()
    items= dict(zip(product_names,product_prices))
    for item in items:
        print(item)

