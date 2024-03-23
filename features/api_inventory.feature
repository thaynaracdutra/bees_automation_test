Feature: API Inventory
  Scenario: List all existing deposits using the /GET method
    Given I have the API endpoint for inventory
    When I make a GET request to the endpoint inventory
    Then I should receive a successful response 200 Code from API

  Scenario: Create a new deposit using the /POST method
    Given I have the API endpoint for inventory
    When I make a POST request to the endpoint with the following deposit data inventory
    Then I should receive a successful response 201 Code from API

  Scenario: Show an existing deposit by ID using the /GET method
    Given I have the API endpoint with ID "1" for inventory
    When I make a GET request to the endpoint inventory
    Then I should receive a successful response 200 Code from API

  Scenario: Update an existing deposit by ID using the /PUT method
    Given I have the API endpoint with ID "165" for inventory
    When I make a PUT request to the endpoint to edit the inventory ID
    Then I should receive a successful response 200 Code from API

  Scenario: Update an existing deposit by ID using the /PATCH method
    Given I have the API endpoint with ID "165" for inventory
    When I make a PATCH request to the endpoint to edit the item ID inventory
    Then I should receive a successful response 200 Code from API

  Scenario: Delete an existing deposit by ID using the /DELETE method
    Given I have the API endpoint for inventory
    When I make a DELETE request to the endpoint inventory
    Then I should receive a successful response 204 Code from API
