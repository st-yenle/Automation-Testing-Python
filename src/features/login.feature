Feature: Login
  Test for Login feature

  Background: Open Login Page
    Given I have navigated to the "login" page

  Scenario: Verify login page contents are correct
    Then The page title is "Sign in to GitHub · GitHub"
    And The page contain "Sign in to GitHub"
    And The page displays "login_field"
    And The page displays "password"

  Scenario Outline: Login
    Given I have navigated to the "login" page
    When I enter a username of "<username>"
    And I enter a password of "<password>"
    And I click on login button
    Then The page title is "<title>"
    Examples:
      | username    | password  | title                      |
      | yenle       | 1234444   | Sign in to GitHub · GitHub |
      | Ngocyenn123 | Abcd999!@ | GitHub                     |

