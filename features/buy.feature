Feature: Buy Functionality
  Scenario: By using Buy Tab,choose the preferred location
    Given I open the application URL in th browser
    When I entered the preferred locations in search tab
    And I Navigate and click on the search tab
    Then I Get the properties based on locations

  Scenario: Get an agent for an preferred location
    Given I open the application URL in th browser
    When I entered the preferred locations in search tab
    And I want to find an agent
    Then I can get a contact of a agent for a given location

  Scenario: Based on budget and location choose the property
    Given I open the application URL in th browser
    When I want to give an Minimum and Maximum budgets levels
    And I want to click on the search tab
    Then Properties for the given location are shown

  Scenario: Compare the properties based on location
    Given I open the application URL in th browser
    And I navigate to the Tips and guides Tab
    When I want to select Two locations based on my interest
    And I navigate to the compare tab
    Then I can able to Compare the two properties based on locations

  Scenario: View the Prop worth option
    Given I open the application URL in th browser
    When I want to click the Prop worth button
    Then I can able to see Prop worth page is shown for selected locations

  Scenario: View the rates and trends
    Given I open the application URL in th browser
    When I want to click on the rates and trends
    Then I can able to see the rates and trends option