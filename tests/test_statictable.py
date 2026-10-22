from playwright.sync_api import Page, expect


def test_rows(page: Page, base_url: str):
    page.goto(base_url)
    table = page.locator("table[name='BookTable'] tbody")
    rows = table.locator("tr")
    row_count = rows.all().count()
    expect(rows).to_have_count(row_count)


def test_columns(page: Page, base_url: str):
    page.goto(base_url)
    table = page.locator("table[name='BookTable'] tbody")
    columns = table.locator("tr").first.locator("th")
    expect(columns).to_have_count(4)


def test_secondrow(page: Page, base_url: str):
    page.goto(base_url)
    table = page.locator("table[name='BookTable'] tbody")
    second_row = table.locator("tr").nth(2)
    expect(second_row).to_be_visible()
    print(second_row.inner_text())


def test_alldata(page: Page, base_url: str):
    page.goto(base_url)
    table = page.locator("table[name='BookTable'] tbody")
    rows = table.locator("tr")
    for row in rows.all():
        print(row.inner_text())


def test_authormukesh(page: Page, base_url: str):
    page.goto(base_url)
    rows = page.locator("table[name='BookTable'] tbody tr")
    matching_books = []
    for row in rows.all():
        if row.locator("td").nth(1).inner_text().strip() == "Mukesh":
            matching_books.append(row.locator("td").first.inner_text())

    assert matching_books, "No books by Mukesh were found"
    print(matching_books)


def test_totalprice(page: Page, base_url: str):
    page.goto(base_url)
    table = page.locator("table[name='BookTable'] tbody")
    rows = table.locator("tr")
    total_price = 0
    for row in rows.all():
        price = row.locator("td").nth(3).inner_text()
        total_price += int(price.strip())
    expect(rows.first).to_be_visible()
    print(f"Total Price: {total_price}")
