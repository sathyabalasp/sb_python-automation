# Created by Sathyaprabha at 8/16/23
Feature: Testing scenario for verifying Products Name and Image
  Verifying every product on Amazon Results page has a Name and a Image

  Scenario: Verifying every product on Amazon Results page has a Name and a Image
    Given Open Amazon page
    When Search for vitamin d
    Then Verify search result is "vitamin d"
    Then Verify every product has a name and  an image
    
  
  Scenario Outline: User can select and search in a department
    Given Open Amazon page
#    When Click on All Department dropdown
    When Select department by alias <dept_name>
    When Search for <product_name>
    Then Verify <search_dept> department is selected
    Examples:
    |dept_name    | product_name    |search_dept   |
    |Baby         | girls bows      |Baby          |
    |Books        | girls books     |Books         |

