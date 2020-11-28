Feature: Claim Query

  Scenario: Success Claim Query
    Given User get access token
    When User send request claim query
    Then Response should be 200 Success