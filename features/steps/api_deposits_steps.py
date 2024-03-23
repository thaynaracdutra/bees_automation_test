import requests
from behave import *
from config import API_DEPOSITS_URL

latest_deposit_id = None


@given('I have the API endpoint')
def step_impl(context):
    context.endpoint = f"{API_DEPOSITS_URL}{'.json'}"


@given('I have the API endpoint with ID "160"')
def step_impl(context):
    context.endpoint = f"{API_DEPOSITS_URL}{'/160.json'}"


@given('I have the API endpoint with ID "165"')
def step_impl(context):
    context.endpoint = f"{API_DEPOSITS_URL}{'/165.json'}"


@when('I make a GET request to the endpoint')
def step_impl(context):
    context.response = requests.get(context.endpoint)


@when('I make a POST request to the endpoint with the following deposit data')
def step_impl(context):
    global latest_deposit_id
    deposit_data = {
        "name": "Zé",
        "address": "Zé street",
        "city": "Zé city",
        "state": "Zé state",
        "zipcode": "Zé zipcode"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(context.endpoint, json=deposit_data, headers=headers)
    latest_deposit_id = context.response.json()['id']


@when('I make a DELETE request to the endpoint')
def step_impl(context):
    global latest_deposit_id
    delete_url = f"{API_DEPOSITS_URL}/{latest_deposit_id}.json"
    response = requests.delete(delete_url)
    context.response = response


@when('I make a  PUT request to the endpoint to edit the name')
def step_impl(context):
    deposit_data = {
        "name": "Zé edit",
        "address": "Zé street",
        "city": "Zé city",
        "state": "Zé state",
        "zipcode": "Zé zipcode"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.put(context.endpoint, json=deposit_data, headers=headers)


@when('I delete a created deposit')
def step_impl(context):
    global latest_deposit_id
    delete_url = f"{context.endpoint}/{latest_deposit_id}"
    response = requests.delete(delete_url)
    context.response = response


@when('I make a PATCH request to the endpoint to edit the city')
def step_impl(context):
    deposit_data = {
        "name": "Zé",
        "address": "Zé street",
        "city": "Zé city edit",
        "state": "Zé state",
        "zipcode": "Zé zipcode"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.patch(context.endpoint, json=deposit_data, headers=headers)


@then('I should receive a successful response 200 Code')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"


@then('I should receive a successful response 201 Code')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"


@then('I should receive a successful response 204 Code')
def step_impl(context):
    assert context.response.status_code == 204, f"Expected status code 204, but got {context.response.status_code}"
