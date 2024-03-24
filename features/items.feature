Feature: Items
  Scenario: Successfully creating a new item
    Given I access the items page
    When I click on create new item, fill out the form with valid data, and submit the form
    Then I see the message indicating that a new item has been successfully created
