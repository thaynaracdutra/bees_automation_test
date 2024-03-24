import requests
from behave import *
from config import API_DEPOSITS_URL

latest_deposit_id = None


@given('the API endpoint is available')
def step_impl(context):
    context.endpoint = f"{API_DEPOSITS_URL}{'.json'}"


@given('the API endpoint for inventory is available with a specific ID under Deposits')
def step_impl(context):
    context.endpoint = f"{API_DEPOSITS_URL}{'/246.json'}"


@given('the API endpoint for inventory is available with an existing ID under Deposits')
def step_impl(context):
    context.endpoint = f"{API_DEPOSITS_URL}{'/246.json'}"


@when('I send a GET request to the endpoint')
def step_impl(context):
    context.response = requests.get(context.endpoint)


@when('I send a POST request to the endpoint with the following deposit data')
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


@when('I send a DELETE request to the endpoint')
def step_impl(context):
    global latest_deposit_id
    delete_url = f"{API_DEPOSITS_URL}/{latest_deposit_id}.json"
    response = requests.delete(delete_url)
    context.response = response


@when('I send a PUT request to the endpoint to update the address')
def step_impl(context):
    deposit_data = {
        "address": "Update Address",
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.put(context.endpoint, json=deposit_data, headers=headers)


@when('I send a PATCH request to the endpoint to update the city')
def step_impl(context):
    deposit_data = {
        "city": "Update city",
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.patch(context.endpoint, json=deposit_data, headers=headers)


@then('I should receive a successful response with status code 200')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"


@then('I expect to receive a successful response with status code 201')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"


@then('I should receive a successful response with status code 204')
def step_impl(context):
    assert context.response.status_code == 204, f"Expected status code 204, but got {context.response.status_code}"
