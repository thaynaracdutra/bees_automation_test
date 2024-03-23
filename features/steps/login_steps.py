from selenium.webdriver import Chrome
from pages.login_page import LoginPage
from behave import *
from pages.home_page import HomePage


@given('I am on the login page')
def step_impl(context):
    context.driver = Chrome()
    context.login_page = LoginPage(context.driver)
    context.driver.get("https://test-bees.herokuapp.com/users/sign_in")
    context.driver.maximize_window()
    context.login_page.is_login_displayed()


@when('I login with the valid credentials')
def step_when(context):
    context.email = context.login_page.email
    context.password = context.login_page.password
    context.login_page.fill_form_login(context.email, context.password)
    context.login_page.submit_login()


@then('I should be logged in successfully')
def step_then(context):
    context.home_page = HomePage(context.driver)
    context.home_page.is_welcome_message_displayed()
