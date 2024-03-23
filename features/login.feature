Feature: Login
    Scenario: Successful login
      Given I am on the login page
      When I login with the valid credentials
      Then I should be logged in successfully