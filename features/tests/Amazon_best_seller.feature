# Created by Sathyaprabha  at 8/9/23
Feature: open amazon BestSellers page
And verify there are links


  Scenario:  opening amazon BestSellers page and verify there are 5 links in the page
    Given Open Amazon page
    When Click on BestSeller
    Then Verify this page has 4 Links
