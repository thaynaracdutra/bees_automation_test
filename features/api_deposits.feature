Feature: API Deposits
  Scenario: List all existing deposits using the /GET method
    Given I have the API endpoint
    When I make a GET request to the endpoint
    Then I should receive a successful response 200 Code

  Scenario: Create a new deposit using the /POST method
    Given I have the API endpoint
    When I make a POST request to the endpoint with the following deposit data
    Then I should receive a successful response 201 Code

  Scenario: Show an existing deposit by ID using the /GET method
    Given I have the API endpoint with ID "160"
    When I make a GET request to the endpoint
    Then I should receive a successful response 200 Code

  Scenario: Update an existing deposit by ID using the /PUT method
    Given I have the API endpoint with ID "165"
    When I make a  PUT request to the endpoint to edit the name
    Then I should receive a successful response 200 Code

  Scenario: Update an existing deposit by ID using the /PATCH method
    Given I have the API endpoint with ID "165"
    When I make a PATCH request to the endpoint to edit the city
    Then I should receive a successful response 200 Code

  Scenario: Delete an existing deposit by ID using the /DELETE method
    Given I have the API endpoint
    When I make a DELETE request to the endpoint
    Then I should receive a successful response 204 Code
