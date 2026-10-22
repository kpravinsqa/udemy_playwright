from playwright.sync_api import expect, Page
import re

def test_scenario_1_cpu_load_of_chrome_should_match_yellow_label(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    cpu_load=""
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        if process_name == "Chrome":
            cpu_load = row.locator("td", has_text="%").inner_text()
            break

    expect(page.locator("strong.chrome-cpu")).to_contain_text(cpu_load)


def test_scenario_2_memory_usage_of_firefox_should_match_blue_label(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()

    memory_usage=""
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        if process_name == "Firefox":
            #memory_usage = row.locator("td", has_text="MB").inner_text() #Here MB is matching with 3 elements. so use regex like below
            memory_usage = row.locator("td", has_text=re.compile("MB$")).inner_text()  # Regex match for values ending with 'MB'
            break

    expect(page.locator("strong.firefox-memory")).to_contain_text(memory_usage)


def test_scenario_3_network_speed_of_chrome_should_match_orange_label(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    network_speed=""
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        if process_name == "Chrome":
            network_speed = row.locator("td", has_text="Mbps").inner_text()
            break
    expect(page.locator("strong.chrome-network")).to_contain_text(network_speed)


def test_scenario_4_disk_space_of_firefox_should_match_violet_label(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    disk_space=""
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        if process_name == "Firefox":
            disk_space = row.locator("td", has_text="MB/s").inner_text()
            break

    expect(page.locator("strong.firefox-disk")).to_contain_text(disk_space)