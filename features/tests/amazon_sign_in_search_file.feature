# Created by sathyaprabha at 8/1/23
Feature: Test Scenarios for SignIn


  Scenario: Verify clicking Returns and Orders  takes to Sign In
     Given Open amazon page
     When Click Returns and Orders

  Scenario:Sign In page can be opened from SignIn popup
     Given Open Amazon page
     When Click on button from SignIn popup
     Then Verify Sign in page opened

  Scenario:Amazon users see sign in button
     Given Open amazon page
     Then Verify Sign in is clickable
     When wait for 3 sec
     Then Verify Sign in is clickable
     When wait for 3 sec
     Then Verify Sign in disappears



