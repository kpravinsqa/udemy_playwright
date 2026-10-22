import os

from playwright.sync_api import Playwright,Page, expect

def test_downloadfile(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    text = "I am AI QA / SDET"
    page.locator("#inputText").fill(text)
    page.locator("#generateTxt").click()

    def handle_download(download):
        download.save_as("downloads/downloaded_file.txt")
    page.on("download", handle_download)
    if page.locator("#txtDownloadLink").is_visible():
        page.locator("#txtDownloadLink").click()
    else :
        print("Download link is not visible")

    page.wait_for_timeout(5000)

    if os.path.exists("downloads/downloaded_file.txt"):
        print("File downloaded successfully")
    else:
        print("File download failed")

    page.wait_for_timeout(5000)

    file = open("downloads/downloaded_file.txt", "r")
    file_text = file.read()
    if file_text == text:
        print("File content is correct")
    else:
        print("File content is incorrect")
