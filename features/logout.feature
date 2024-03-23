Feature: Logout
  Scenario: Successful Logout
    Given I am logged in and on the home page
    When I click the logout button
    Then I should be successfully logged out