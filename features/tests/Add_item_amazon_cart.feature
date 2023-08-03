# Created by Sathyaprabha at 8/1/23
Feature: Test Scenario for adding a product


  Scenario: Verify adding a product to cart and check the cart for number of items
   Given open amazon page
   When Input the product
   Then Select one product
   Then Add it to the cart
   Then Verify product in cart
