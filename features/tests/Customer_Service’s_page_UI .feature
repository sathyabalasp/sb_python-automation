# Created by Sathyaprabha at 8/5/23
Feature: Test scenario for verifying Customer Service's Page UI elements present in the page


  Scenario: Verify Customer Service’s page UI elements are present
    Given Open Amazon page
    Given Open Amazon Customer Service page
    When Check for in issue card UI elements
    Then Verify UI  no of 11 elements
    Then Check for in Search our help library UI elements
    Then Verify other UI links 12 elements
