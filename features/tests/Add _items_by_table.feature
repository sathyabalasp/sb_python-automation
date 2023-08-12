# Created by Sathyaprabha at 8/11/23
Feature:Testing for amazon search for n_number product

  Scenario Outline: testing adding a product to amazon search
    Given open amazon page
    When Search for <product>
    Then Verify search <result> is correct
    Examples:
    |product      |result        |
    |headphones   |"headphones"  |
    |airpods pro  |"airpods pro" |
    |cell phone   |"cell phone"  |