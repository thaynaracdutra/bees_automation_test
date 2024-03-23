import time

from faker import Faker
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.deposits_page import DepositsPage
from selenium.webdriver import Chrome
from behave import *

fake = Faker()


@given('I access the deposits page')
def step_impl(context):
    context.driver = Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.login()
    context.home_page = HomePage(context.driver)
    context.home_page.go_to_deposits_page()
    time.sleep(2)


@when('I click on create new deposit, fill out the form with valid data, and submit the form')
def step_impl(context):
    context.name = fake.company()
    context.address = fake.address()
    context.city = fake.city()
    context.state = fake.state()
    context.zipcode = fake.zip()
    context.deposits_page = DepositsPage(context.driver)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    context.deposits_page.create_new_deposit()
    time.sleep(3)
    context.deposits_page.fill_deposit_form(context.name, context.address, context.city, context.state, context.zipcode)


@then('I see the message indicating that a new deposit has been successfully created')
def step_impl(context):
    assert context.deposits_page.deposit_created_displayed()
