import time
from behave import *
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)


@given('I access the inventory page')
def step_impl(context):
    context.driver = webdriver.Chrome(options=chrome_options)
    context.login_page = LoginPage(context.driver)
    context.login_page.login()
    context.home_page = HomePage(context.driver)
    context.home_page.go_to_inventory_page()
    time.sleep(2)


@given('I access an existing inventory')
def step_impl(context):
    context.home_page.go_to_inventory_page()
    time.sleep(2)
    if not hasattr(context, 'inventory_page'):
        context.inventory_page = InventoryPage(context.driver)


@when('I click on create new inventory, fill out the form with valid data, and submit the form')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.create_new_inventory()
    time.sleep(2)
    context.inventory_page.fill_inventory_form()
    context.inventory_page.submit_new_inventory()


@when('I destroy the current inventory')
def step_impl(context):
    context.inventory_page.access_the_created_inventory()
    time.sleep(5)
    context.inventory_page.destroy_the_inventory()


@then('I see the message indicating that a new inventory has been successfully created')
def step_impl(context):
    assert context.inventory_page.inventory_created_displayed()


@then('I see the message indicating that inventory has been successfully destroyed')
def step_impl(context):
    assert context.inventory_page.inventory_destroyed_displayed()
