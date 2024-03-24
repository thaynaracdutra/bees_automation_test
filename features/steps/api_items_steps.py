import requests
from behave import *
from config import API_ITEMS_URL

latest_item_id = None


@given('the API endpoint for items is available')
def step_impl(context):
    context.endpoint = f"{API_ITEMS_URL}{'.json'}"


@given('the API endpoint for inventory is available with a specific ID under Items')
def step_impl(context):
    context.endpoint = f"{API_ITEMS_URL}{'/160.json'}"


@given('the API endpoint for inventory is available with an existing ID under Items')
def step_impl(context):
    context.endpoint = f"{API_ITEMS_URL}{'/160.json'}"


@when('I send a GET request to the items endpoint')
def step_impl(context):
    context.response = requests.get(context.endpoint)


@when('I send a POST request to the items endpoint with the following items data')
def step_impl(context):
    global latest_item_id
    item_data = {
        "name": "Brahma",
        "height": "0.8",
        "width": "0.8",
        "weight": "0.8"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(context.endpoint, json=item_data, headers=headers)
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"
    latest_item_id = context.response.json().get('id')


@when('I send a DELETE request to the items endpoint')
def step_impl(context):
    global latest_item_id
    delete_url = f"{API_ITEMS_URL}/{latest_item_id}.json"
    context.response = requests.delete(delete_url)


@when('I send a PUT request to the items endpoint to edit the width')
def step_impl(context):
    items_data = {
        "width": "0.9"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.put(context.endpoint, json=items_data, headers=headers)


@when('I send a PATCH request to the items endpoint to edit the height')
def step_impl(context):
    items_data = {
        "height": "0.9"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.patch(context.endpoint, json=items_data, headers=headers)


@then('I should receive a successful response with status code 200 from the Items API')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"


@then('I should receive a successful response with status code 201 from the Items API')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"


@then('I should receive a successful response with status code 204 from the Items API')
def step_impl(context):
    assert context.response.status_code == 204, f"Expected status code 204, but got {context.response.status_code}"
