# Created by Sathyaprabha at 8/1/23
Feature: Verifying Amazon Cart

  Scenario: verifies that users Amazon Cart is empty
    Given Open amazon page
    When clicks on the cart icon
    Then Verify Your Amazon Cart is empty text present
