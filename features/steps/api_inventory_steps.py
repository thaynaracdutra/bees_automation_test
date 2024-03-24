import requests
from behave import *
from config import API_INVENTORIES_URL

latest_inventory_id = None


@given('the API endpoint for inventory is available')
def step_impl(context):
    context.endpoint = f"{API_INVENTORIES_URL}.json"


@given('the API endpoint for inventory is available with a specific ID under Inventory')
def step_impl(context):
    context.endpoint = f"{API_INVENTORIES_URL}/124.json"


@given('the API endpoint for inventory is available with an existing ID under Inventory')
def step_impl(context):
    context.endpoint = f"{API_INVENTORIES_URL}/124.json"


@when('I send a GET request to the inventory endpoint')
def step_impl(context):
    context.response = requests.get(context.endpoint)


@when('I send a POST request to the inventory endpoint with the following inventory data')
def step_impl(context):
    global latest_inventory_id
    inventory_data = {
        "item_id": 166,
        "deposit_id": 253,
        "item_count": 100
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(context.endpoint, json=inventory_data, headers=headers)
    latest_inventory_id = context.response.json()['id']


@when('I send a DELETE request to the inventory endpoint')
def step_impl(context):
    global latest_inventory_id
    delete_url = f"{API_INVENTORIES_URL}/{latest_inventory_id}.json"
    response = requests.delete(delete_url)
    context.response = response


@when('I send a PUT request to the inventory endpoint to update the inventory ID')
def step_impl(context):
    global latest_inventory_id
    put_url = f"{API_INVENTORIES_URL}/124.json"
    inventory_data = {
        "item_count": 100
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.put(put_url, json=inventory_data, headers=headers)


@when('I send a PATCH request to the inventory endpoint to update the item ID')
def step_impl(context):
    global latest_inventory_id
    patch_url = f"{API_INVENTORIES_URL}/124.json"
    inventory_data = {
        "item_count": 101
    }
    headers = {'Content-Type': 'application/json'}
    context.response = requests.patch(patch_url, json=inventory_data, headers=headers)


@then('I should receive a successful response with status code 200 from the API')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"


@then('I should receive a successful response with status code 201 from the API')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"


@then('I should receive a successful response with status code 204 from the API')
def step_impl(context):
    assert context.response.status_code == 204, f"Expected status code 204, but got {context.response.status_code}"
