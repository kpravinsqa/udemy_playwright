from playwright.sync_api import Page, expect

def test_upload_single(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#singleFileInput").set_input_files("downloads/downloaded_file.txt")
    page.locator("#singleFileForm button").click()
    expect(page.locator("#singleFileStatus")).to_contain_text("downloaded_file.txt")