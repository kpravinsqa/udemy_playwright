from playwright.sync_api import Page,expect

def test_dragndrop(page:Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")
    debit_account_type = page.locator(".button.button-orange").nth(4)
    debit_account_target = page.locator(".field14.ui-droppable.ui-sortable")
    debit_account_type.drag_to(debit_account_target)
    debit_amount_source = page.locator(".button.button-orange").nth(1)
    debit_amount_target = page.locator(".field13.ui-droppable.ui-sortable").nth(0)
    debit_amount_source.drag_to(debit_amount_target)
    credit_account_source = page.locator('.button.button-orange').nth(5)
    credit_account_target = page.locator('.field15.ui-droppable.ui-sortable')
    credit_account_source.drag_to(credit_account_target)
    credit_amount_source = page.locator('.button.button-orange').nth(3)
    credit_amount_target = page.locator('.field13.ui-droppable.ui-sortable').nth(1)
    credit_amount_source.drag_to(credit_amount_target)

    expect(page.locator('.button.button-green').nth(0)).to_be_visible()