# Created by Sathyaprabha  at 8/9/23
Feature: open amazon BestSellers page
And verify top menu pages are opening


  Scenario:  Opening Amazon BestSellers page and verify top menu pages are opening
    Given Open Amazon page
    When Click on BestSeller
    Then Verify this page has 5 top menu
    Then Verify each 5 top menus pages opens

