import time

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.items_page import ItemsPage
from selenium.webdriver import Chrome
from behave import *


@given('I access the items page')
def step_impl(context):
    context.driver = Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.login()
    context.home_page = HomePage(context.driver)
    context.home_page.go_to_items_page()
    time.sleep(2)


@when('I click on create new item, fill out the form with valid data, and submit the form')
def step_impl(context):
    context.items_page = ItemsPage(context.driver)
    context.items_page.create_new_item()
    time.sleep(2)
    context.items_page.fill_item_form()
    context.items_page.submit_new_item()


@then('I see the message indicating that a new item has been successfully created')
def step_impl(context):
    assert context.items_page.item_created_displayed()
