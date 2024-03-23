Feature: Deposits
  Scenario: Successfully creating a new deposit
    Given I access the deposits page
    When I click on create new deposit, fill out the form with valid data, and submit the form
    Then I see the message indicating that a new deposit has been successfully created