from faker import Faker
from selenium.webdriver import Chrome
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from behave import *

fake = Faker()


@given('I am on the registration page')
def step_impl(context):
    context.driver = Chrome()
    context.registration_page = RegistrationPage(context.driver)
    context.driver.get("https://test-bees.herokuapp.com/users/sign_up")
    context.driver.maximize_window()


@when('I fill the registration form and submit')
def step_when(context):
    context.email = fake.email()
    context.password = fake.password()
    context.registration_page.fill_form(context.email, context.password, context.password)
    context.registration_page.submit_registration()


@then('I should be registered and view the welcome message "Welcome to your storage"')
def step_then(context):
    context.home_page = HomePage(context.driver)
    context.home_page.is_welcome_message_displayed()
