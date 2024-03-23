import requests
from behave import *
from config import API_INVENTORIES_URL

latest_inventory_id = None


@given('I have the API endpoint for inventory')
def step_impl(context):
    context.endpoint = f"{API_INVENTORIES_URL}.json"


@given('I have the API endpoint with ID "1" for inventory')
def step_impl(context):
    context.endpoint = f"{API_INVENTORIES_URL}/1.json"


@given('I have the API endpoint with ID "165" for inventory')
def step_impl(context):
    context.endpoint = f"{API_INVENTORIES_URL}/165.json"


@when('I make a GET request to the endpoint inventory')
def step_impl(context):
    context.response = requests.get(context.endpoint)


@when('I make a POST request to the endpoint with the following deposit data inventory')
def step_impl(context):
    global latest_inventory_id
    inventory_data = {
        "item_id": 105,
        "deposit_id": 168,
        "item_count": 100
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(context.endpoint, json=inventory_data, headers=headers)
    latest_inventory_id = context.response.json()['id']


@when('I make a DELETE request to the endpoint inventory')
def step_impl(context):
    global latest_inventory_id
    delete_url = f"{API_INVENTORIES_URL}/{latest_inventory_id}.json"
    response = requests.delete(delete_url)
    context.response = response


@when('I make a PUT request to the endpoint to edit the inventory ID')
def step_impl(context):
    global latest_inventory_id
    put_url = f"{API_INVENTORIES_URL}/{latest_inventory_id}.json"
    inventory_data = {
        "item_id": 102,
        "deposit_id": 163,
        "item_count": 99
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.put(put_url, json=inventory_data, headers=headers)


@when('I make a PATCH request to the endpoint to edit the item ID inventory')
def step_impl(context):
    global latest_inventory_id
    patch_url = f"{API_INVENTORIES_URL}/{latest_inventory_id}.json"
    inventory_data = {
        "item_id": 102,
        "deposit_id": 163,
        "item_count": 98
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.patch(patch_url, json=inventory_data, headers=headers)


@then('I should receive a successful response 200 Code from API')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"


@then('I should receive a successful response 201 Code from API')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"


@then('I should receive a successful response 204 Code from API')
def step_impl(context):
    assert context.response.status_code == 204, f"Expected status code 204, but got {context.response.status_code}"
