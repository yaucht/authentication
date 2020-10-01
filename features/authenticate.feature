Feature: Authentication handler

    Scenario: OK
        Given recognizable credentials
        When we request a token
        Then service will respond with 200 status code
        And we will get a JWT

    Scenario: Unrecognizable credentials
        Given unrecognizable credentials
        When we request a token
        Then service will respond with 403 status code


    Scenario Outline: Malformed credentials
        Given we use <username> and <password>
        When we request a token
        Then service will respond with <code> status code

        Examples: 
            | username | password | code |
            | invalid+ | valid    | 422  |
            | valid    | invalid+ | 422  |
            | invalid+ | invalid+ | 422  |
            # But unrecognizable
            | valid    | valid    | 403  |
