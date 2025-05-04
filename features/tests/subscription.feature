# Created by joshzz at 5/3/25
Feature: Access Subscription Page

  Scenario: User can open Subscription & payments page
    Given the user is on the main page and already logged in
    When the user navigates to the Subscription & payments page
    Then the Subscription & payments page should be displayed
    And the "Back" and "Upgrade Plan" buttons should be visible