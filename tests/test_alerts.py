# from playwright.sync_api import Page, expect
#
#
# URL = "https://testautomationpractice.blogspot.com/"
#
#
# def test_simple_alert_with_event_handler(page: Page):
#     page.goto(URL)
#     dialog_details = {}
#
#     def handle_dialog(dialog):
#         dialog_details["type"] = dialog.type
#         dialog_details["message"] = dialog.message
#         dialog.accept()
#
#     page.on("dialog", handle_dialog)
#     page.locator("#alertBtn").click()
#
#     assert dialog_details == {
#         "type": "alert",
#         "message": "I am an alert box!",
#     }
#
#
# def test_simple_alert_with_lambda_handler(page: Page):
#     page.goto(URL)
#     dialogs = []
#     page.on(
#         "dialog",
#         lambda dialog: (dialogs.append((dialog.type, dialog.message)), dialog.accept()),
#     )
#     page.locator("#alertBtn").click()
#
#     assert dialogs == [("alert", "I am an alert box!")]
#
#
# def test_confirmation_alert_with_event_handler(page: Page):
#     page.goto(URL)
#     dialog_details = {}
#
#     def handle_dialog(dialog):
#         dialog_details["type"] = dialog.type
#         dialog_details["message"] = dialog.message
#         dialog.accept()
#
#     page.on("dialog", handle_dialog)
#     page.locator("#confirmBtn").click()
#
#     assert dialog_details == {"type": "confirm", "message": "Press a button!"}
#     expect(page.locator("#demo")).to_have_text("You pressed OK!")
#
#
# def test_confirmation_alert_with_lambda_handler(page: Page):
#     page.goto(URL)
#     dialogs = []
#     page.on(
#         "dialog",
#         lambda dialog: (dialogs.append((dialog.type, dialog.message)), dialog.dismiss()),
#     )
#     page.locator("#confirmBtn").click()
#
#     assert dialogs == [("confirm", "Press a button!")]
#     expect(page.locator("#demo")).to_have_text("You pressed Cancel!")
#
#
# def test_prompt_alert_with_event_handler(page: Page):
#     page.goto(URL)
#     prompt_text = "Playwright User"
#     dialog_details = {}
#
#     def handle_dialog(dialog):
#         dialog_details["type"] = dialog.type
#         dialog_details["message"] = dialog.message
#         dialog_details["default_value"] = dialog.default_value
#         dialog.accept(prompt_text)
#
#     page.on("dialog", handle_dialog)
#     page.locator("#promptBtn").click()
#
#     assert dialog_details == {
#         "type": "prompt",
#         "message": "Please enter your name:",
#         "default_value": "Harry Potter",
#     }
#     expect(page.locator("#demo")).to_have_text(
#         f"Hello {prompt_text}! How are you today?"
#     )
#
#
# def test_prompt_alert_with_lambda_handler(page: Page):
#     page.goto(URL)
#     prompt_text = "Lambda User"
#     dialogs = []
#     page.on(
#         "dialog",
#         lambda dialog: (
#             dialogs.append((dialog.type, dialog.message, dialog.default_value)),
#             dialog.accept(prompt_text),
#         ),
#     )
#     page.locator("#promptBtn").click()
#
#     assert dialogs == [
#         ("prompt", "Please enter your name:", "Harry Potter")
#     ]
#     expect(page.locator("#demo")).to_have_text(
#         f"Hello {prompt_text}! How are you today?"
#     )
#
#     #myscript

from playwright.sync_api import Playwright, Page, expect

def test_simple_alert(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    dialog_details = {}

    def handle_dialog(dialog):
        dialog_details["type"] = dialog.type
        dialog_details["message"] = dialog.message
        dialog.accept()

    page.on("dialog", handle_dialog)
    page.locator("#alertBtn").click()

    assert dialog_details == {"type": "alert", "message": "I am an alert box!"}