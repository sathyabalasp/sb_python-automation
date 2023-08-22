# Created by sathyaprabha at 8/1/23
Feature: Test Scenarios for Sign In through Returns and Orders


  Scenario: Verify clicking Returns and Orders  takes to Sign In
    Given Open amazon page
    When Click Returns and Orders
    Then Verify Sign in page opened
    Then Verify Email input field is present



