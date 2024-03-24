Feature: API Items
  Scenario: List all existing items via the /GET method
    Given the API endpoint for items is available
    When I send a GET request to the items endpoint
    Then I should receive a successful response with status code 200 from the Items API

  Scenario: Create a new item via the /POST method
    Given the API endpoint for items is available
    When I send a POST request to the items endpoint with the following items data
    Then I should receive a successful response with status code 201 from the Items API

  Scenario: Retrieve an existing item by ID via the /GET method
    Given the API endpoint for inventory is available with a specific ID under Items
    When I send a GET request to the items endpoint
    Then I should receive a successful response with status code 200 from the Items API

  Scenario: Update an existing item by ID via the /PUT method
    Given the API endpoint for inventory is available with an existing ID under Items
    When I send a PUT request to the items endpoint to edit the width
    Then I should receive a successful response with status code 200 from the Items API

  Scenario: Modify an existing item by ID via the /PATCH method
    Given the API endpoint for inventory is available with an existing ID under Items
    When I send a PATCH request to the items endpoint to edit the height
    Then I should receive a successful response with status code 200 from the Items API

  Scenario: Delete an existing item by ID via the /DELETE method
    Given the API endpoint for items is available
    When I send a DELETE request to the items endpoint
    Then I should receive a successful response with status code 204 from the Items API
