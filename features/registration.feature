Feature: Registration
    Scenario: Successful registration
      Given I am on the registration page
      When I fill the registration form and submit
      Then I should be registered and view the welcome message "Welcome to your storage"