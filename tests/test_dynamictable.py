from playwright.sync_api import Page
import re


def test_cpuload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    table = page.locator("table[id='taskTable'] tbody")
    rows = table.locator("tr").all()
    web_cpu_load =page.locator("div[class='display-values'] p strong").nth(0).inner_text()
    table_cpu_load=""
    for row in rows:
        if row.locator("td").nth(0).inner_text() == "Chrome":
            table_cpu_load = row.locator("td:has-text('%')").inner_text()
    assert(web_cpu_load == table_cpu_load)

def test_memoryusage(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    table = page.locator("table[id='taskTable'] tbody")
    rows = table.locator("tr").all()
    table_memory_usage = ""
    web_memory_usage = page.locator("#displayValues p strong").nth(1).inner_text()
    for row in rows:
        if row.locator("td").nth(0).inner_text() == "Firefox":
            if  row.locator("td",has_text=re.compile("MB$")):
                table_memory_usage = row.locator("td",has_text=re.compile("MB$")).inner_text()
    assert(web_memory_usage == table_memory_usage)





