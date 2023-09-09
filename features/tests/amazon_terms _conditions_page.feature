# Created by Sathyaprabha at 9/8/23
Feature: window handling test case from the class
  And verify that user can open amazon applications from Terms of Conditions


  Scenario: User can open and close Amazon Privacy Notice
    Given Open amazon page
    Given Open Amazon Term and Conditions page
    And Store original windows
    When Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon.com Privacy Notice Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
