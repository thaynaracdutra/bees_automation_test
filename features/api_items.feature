Feature: API Deposits
  Scenario: List all existing deposits using the /GET method
    Given I have the API endpoint for items
    When I make a GET request to the endpoint for items
    Then I should receive a successful response 200 Code from Items API

  Scenario: Create a new deposit using the /POST method
    Given I have the API endpoint for items
    When I make a POST request to the endpoint with the following items data
    Then I should receive a successful response 201 Code from Items API

  Scenario: Show an existing deposit by ID using the /GET method
    Given I have the API endpoint with ID "101"
    When I make a GET request to the endpoint for items
    Then I should receive a successful response 200 Code from Items API

  Scenario: Update an existing deposit by ID using the /PUT method
    Given I have the API endpoint with ID "34"
    When I make a  PUT request to the endpoint to edit the width
    Then I should receive a successful response 200 Code from Items API

  Scenario: I make a PATCH request to the endpoint to edit the height
    Given I have the API endpoint with ID "34"
    When I make a PATCH request to the endpoint to edit the city
    Then I should receive a successful response 200 Code from Items API

  Scenario: Delete an existing item by ID using the /DELETE method
    Given I have the API endpoint for items
    When I make a DELETE request to the endpoint items
    Then I should receive a successful response 204 Code from Items API
