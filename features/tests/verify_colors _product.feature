# Created by Sathyaprabha at 8/16/23
Feature: Testing for product page

  Scenario: Verifying a product's colors by clicking.
   Given Open Amazon product B07BJKRR25 page
   Then Verify user can click through colors

  Scenario: Select a product from Closing category and hover over New Arrivals
    Given open amazon page
    When Search for hoodie for girls
    Then Select one product hoodie
    When Hover over New Arrivals
    Then Verify that the user sees the deals