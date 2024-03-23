import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver import Chrome
from behave import *


@given('I am logged in and on the home page')
def step_impl(context):
    context.driver = Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.login()


@when('I click the logout button')
def step_when(context):
    context.home_page = HomePage(context.driver)
    context.home_page.logout()
    time.sleep(5)
    context.driver.refresh()


@then('I should be successfully logged out')
def step_then(context):
    context.login_page.is_login_displayed()
