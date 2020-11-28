Feature: Claim Query2

  Scenario: Success Claim Query2
    Given User get access token
    When User send request claim query
    Then Response should be 200 Success