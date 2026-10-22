#https://demowebshop.tricentis.com/login

import pytest
from playwright.sync_api import Page,expect

creds = [("laura.taylor1234@example.com", "test123", "valid"),
    ("invaliduser@example.com", "test321", "invalid"),
    ("validuser@example.com", "testxyz", "invalid"),
    ("", "", "invalid")
        ]


@pytest.mark.parametrize("email, password, expected", creds)
def test_login(page: Page, email: str, password: str, expected: str):
    page.goto("https://demowebshop.tricentis.com/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Log in").click()

    if expected == "valid":
        expect(page).to_have_url("https://demowebshop.tricentis.com/")
        expect(page.get_by_role("link", name="Log out")).to_be_visible()
    else:
        expect(page.locator(".validation-summary-errors")).to_be_visible()

import csv


login_data=[]    # empty list

# read csv file
csvfile=open("testdata/data.csv",newline='', encoding='utf-8')
reader=csv.DictReader(csvfile)

for row in reader:
    login_data.append((row["email"],row["password"],row["validity"]))


@pytest.mark.parametrize("email, password, validity", login_data)
def test_login_data_driven_csv(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    #fill teh login form
    page.locator("#Email").fill(email)   # email id
    page.locator("#Password").fill(password)  #password
    page.locator("input[value='Log in']").click()

    #validation
    if validity=="valid":
        logout_link=page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        error_message=page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000) # checking error message
        expect(page).to_have_url("https://demowebshop.tricentis.com/login") # checking same login page

import json

test_data=[]

json_file= open("testdata/testdata.json","r")
json_data = json.load()

for row in json_data:
    test_data.append((row["email"],row["password"],row["validity"]))


@pytest.mark.parametrize("email, password, validity", test_data)
def test_login_data_driven_json(email, password, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/login")

    # fill the login form
    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)
    page.locator("input[value='Log in']").click()

    # validation
    if validity == "valid":
        logout_link = page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        error_message = page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")