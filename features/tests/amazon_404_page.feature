# Created by Sathyaprabha at 9/8/23
Feature: Tests for 404 page

  Scenario: User is able to navigate to amazon blog from 404 page
     Given Open Amazon product B07NF5WGQ11111111 page
     And Store original windows
     When Click on Dog image
     And Switch to new window
     Then Verify blog is opened
     And Close blog
     And Returns to original window
