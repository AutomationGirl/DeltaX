Feature: successfully registered users

  Scenario: successful register with valid credentials in required fields

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username   | Password         | Confirm Password | E-mail             |
      | shivani    | Tyagi     | shivanit28 | shivanityagi2892 | shivanityagi2892 | shivanit@gmail.com |
    And He Click on Submit button

    Then User should be register successfully
    And A successful registration message should show
    And Acknowledgment​ email should send to the user


  Scenario: successful register with valid Credentials in both fields

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username   | Password         | Confirm Password | E-mail             |
      | shivani    | Tyagi     | shivanit28 | shivanityagi2892 | shivanityagi2892 | shivanit@gmail.com |
    And He enter valid values in optional fields
      | Department | Contact No |
      | Sales      | 9620334447 |
    And He Click on Submit button

    Then User should be register successfully
    And A successful registration message should show
    And Acknowledgment​ email should send to the user


  Scenario: successful not register with invalid Credentials in required fields

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username   | Password         | Confirm Password | E-mail             |
      | S          | Ty        | shivanit28 | shivanityagi2892 | shivanityagi2892 | shivanit@gmail.com |
    And He Click on Submit button

    Then Should show error message for invalid data type


  Scenario: user not register with invalid Credentials in both fields

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username | Password | Confirm Password | E-mail  |
      | N          | T         | shivani  | 1234567  | 1234567          | shivani |
    And He enter valid values in optional fields
      | Department | Contact No |
      | Support    | 962033444  |


    Then Submit button should show disabled
    Then Should show error message for invalid data type


  Scenario: user not register with blank Credentials in both fields

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username | Password | Confirm Password | E-mail |
      |            |           |          |          |                  |        |
    And He enter valid values in optional fields
      | Department | Contact No |
      |            |            |


    Then Submit button should show disabled


  Scenario: verify password and confirm password fields

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username  | Password   | Confirm Password | E-mail             |
      | Shalu      | Samal     | shivani28 | shivani28# | 1234567          | shivanit@gmail.com |
    And He enter valid values in optional fields
      | Department | Contact No |
      | Support    | 962033444  |
    And He Click on Submit button


    Then Should show error message password and confirmed password not matched
    And Submit button should show disabled


  Scenario: user not to register with invalid username and password

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username | Password | Confirm Password | E-mail             |
      | SHiv       | Tya       | shivani  | shivani  | shivanityagi2892 | shivanit@gmail.com |
    And He Click on Submit button

    Then Should show error message for invalid data type


  Scenario: user not register with invalid Email id

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username   | Password         | Confirm Password | E-mail   |
      | S          | Ty        | shivanit28 | shivanityagi2892 | shivanityagi2892 | shivanit |
    And He Click on Submit button

    Then Should show error message for invalid data type



  Scenario: user not register with invalid Email id

    When User Navigate to Register Page

    And He Enter values in required fields
      | First Name | Last Name | Username   | Password         | Confirm Password | E-mail   |
      | S          | Ty        | shivanit28 | shivanityagi2892 | shivanityagi2892 | shivanit |
    And He Click on Submit button

    Then Should show error message for invalid data type



