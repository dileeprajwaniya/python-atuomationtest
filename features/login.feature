Feature: User Login

  Scenario: Valid login with username and password
    Given I open the login page
    When I enter username and password
    And I click on the login button
    Then I should see a successful login message

