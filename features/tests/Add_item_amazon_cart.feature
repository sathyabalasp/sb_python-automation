# Created by Sathyaprabha at 8/1/23
Feature: Test Scenario for adding a product


  Scenario: Verify adding a product to cart and check the cart for number of items
   Given Open Amazon page
   When Input the product
   Then Select one product
   When wait for 3 sec
   Then Add it to the cart
   When wait for 3 sec
   Then Verify Subtotal (1 item): number of present

