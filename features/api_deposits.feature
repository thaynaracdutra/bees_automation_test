Feature: API Deposits

  Scenario: List all existing deposits via the /GET method
    Given the API endpoint is available
    When I send a GET request to the endpoint
    Then I should receive a successful response with status code 200

  Scenario: Create a new deposit via the /POST method
    Given the API endpoint is available
    When I send a POST request to the endpoint with the following deposit data
    Then I expect to receive a successful response with status code 201

  Scenario: Retrieve an existing deposit by ID via the /GET method
    Given the API endpoint for inventory is available with a specific ID under Deposits
    When I send a GET request to the endpoint
    Then I should receive a successful response with status code 200

  Scenario: Update an existing deposit by ID via the /PUT method
    Given the API endpoint for inventory is available with an existing ID under Deposits
    When I send a PUT request to the endpoint to update the address
    Then I should receive a successful response with status code 200

  Scenario: Modify an existing deposit by ID via the /PATCH method
    Given the API endpoint for inventory is available with an existing ID under Deposits
    When I send a PATCH request to the endpoint to update the city
    Then I should receive a successful response with status code 200

  Scenario: Delete an existing deposit by ID via the /DELETE method
    Given the API endpoint is available
    When I send a DELETE request to the endpoint
    Then I should receive a successful response with status code 204
