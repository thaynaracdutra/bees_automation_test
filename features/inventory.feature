Feature: Inventory
  Scenario: Successfully creating a new inventory
    Given I access the inventory page
    When I click on create new inventory, fill out the form with valid data, and submit the form
    Then I see the message indicating that a new inventory has been successfully created

  Scenario: Delete an existing inventory
    Given I access the inventory page
    And I access an existing inventory
    When I destroy the current inventory
    Then I see the message indicating that inventory has been successfully destroyed