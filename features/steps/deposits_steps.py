import time

from faker import Faker
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.deposits_page import DepositsPage
from behave import *
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


fake = Faker()


@given('I access the deposits page')
def step_impl(context):
    context.driver = webdriver.Chrome(options=chrome_options)
    context.login_page = LoginPage(context.driver)
    context.login_page.login()
    time.sleep(5)
    context.home_page = HomePage(context.driver)
    context.home_page.go_to_deposits_page()
    time.sleep(5)


@when('I click on create new deposit, fill out the form with valid data, and submit the form')
def step_impl(context):
    context.name = fake.company()
    context.address = fake.address()
    context.city = fake.city()
    context.state = fake.state()
    context.zipcode = fake.zip()
    context.deposits_page = DepositsPage(context.driver)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    context.deposits_page.create_new_deposit()
    time.sleep(5)
    context.deposits_page.fill_deposit_form(context.name, context.address, context.city, context.state)


@then('I see the message indicating that a new deposit has been successfully created')
def step_impl(context):
    assert context.deposits_page.deposit_created_displayed()
