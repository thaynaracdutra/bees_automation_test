Feature: API Inventory

  Scenario: List all existing inventory via the /GET method
    Given the API endpoint for inventory is available
    When I send a GET request to the inventory endpoint
    Then I should receive a successful response with status code 200 from the API

  Scenario: Create a new inventory via the /POST method
    Given the API endpoint for inventory is available
    When I send a POST request to the inventory endpoint with the following inventory data
    Then I should receive a successful response with status code 201 from the API

  Scenario: Retrieve an existing inventory by ID via the /GET method
    Given the API endpoint for inventory is available with a specific ID under Inventory
    When I send a GET request to the inventory endpoint
    Then I should receive a successful response with status code 200 from the API

  Scenario: Update an existing inventory by ID via the /PUT method
    Given the API endpoint for inventory is available with an existing ID under Inventory
    When I send a PUT request to the inventory endpoint to update the inventory ID
    Then I should receive a successful response with status code 200 from the API

  Scenario: Modify an existing inventory by ID via the /PATCH method
    Given the API endpoint for inventory is available with an existing ID under Inventory
    When I send a PATCH request to the inventory endpoint to update the item ID
    Then I should receive a successful response with status code 200 from the API

  Scenario: Delete an existing inventory by ID via the /DELETE method
    Given the API endpoint for inventory is available
    When I send a DELETE request to the inventory endpoint
    Then I should receive a successful response with status code 204 from the API
