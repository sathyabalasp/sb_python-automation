# Created by balamurugann at 8/16/23
Feature: Testing scenario for verifying Products Name and Image
  Verifying every product on Amazon Results page has a Name and a Image

  Scenario: Verifying every product on Amazon Results page has a Name and a Image
    Given Open Amazon page
    When Search for coffee
    Then Verify every product has name and image
