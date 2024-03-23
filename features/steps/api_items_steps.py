import requests
from behave import *
from config import API_ITEMS_URL

latest_item_id = None


@given('I have the API endpoint for items')
def step_impl(context):
    context.endpoint = f"{API_ITEMS_URL}{'.json'}"


@given('I have the API endpoint with ID "101"')
def step_impl(context):
    context.endpoint = f"{API_ITEMS_URL}{'/101.json'}"


@given('I have the API endpoint with ID "34"')
def step_impl(context):
    context.endpoint = f"{API_ITEMS_URL}{'/34.json'}"


@when('I make a GET request to the endpoint for items')
def step_impl(context):
    context.response = requests.get(context.endpoint)


@when('I make a POST request to the endpoint with the following items data')
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


@when('I make a DELETE request to the endpoint items')
def step_impl(context):
    global latest_item_id
    delete_url = f"{API_ITEMS_URL}/{latest_item_id}.json"
    context.response = requests.delete(delete_url)


@when('I make a  PUT request to the endpoint to edit the width')
def step_impl(context):
    items_data = {
        "width": "0.9"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.put(context.endpoint, json=items_data, headers=headers)


@when('I make a PATCH request to the endpoint to edit the height')
def step_impl(context):
    items_data = {
        "height": "0.9"
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.patch(context.endpoint, json=items_data, headers=headers)


@then('I should receive a successful response 200 Code from Items API')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"


@then('I should receive a successful response 201 Code from Items API')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"


@then('I should receive a successful response 204 Code from Items API')
def step_impl(context):
    assert context.response.status_code == 204, f"Expected status code 204, but got {context.response.status_code}"
