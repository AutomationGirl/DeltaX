from behave import *
from pages.register_page import RegisterUser
registerUser = RegisterUser()

use_step_matcher("re")


@step("User Navigate to Register Page")
def step_impl(context):
    registerUser.user_navigation()




@step("He Enter values in required fields")
def step_impl(context):
    table = context.table
    row = table[0]
    params = {
        'first_name': row['First Name'],
        'last_name': row['Last Name'],
        'username': row['Username'],
        'password': row['Password'],
        'confirm_password': row['Confirm Password'],
        'email_id': row['E-mail'],

    }

    registerUser.set_required_fields_data(params)


@step("He enter valid values in optional fields")
def step_impl(context):
    table = context.table
    row = table[0]
    params = {

        'Department': row['Department'],
        'contact_no': row['Contact No']
    }

    registerUser.set_optional_fields_data(params)


@step("He Click on Submit button")
def step_impl(context):
    registerUser.click_on_submit()


@then("User should be register successfully")
def step_impl(context):
    pass


@step("A successful registration message should show")
def step_impl(context):
    registerUser.verify_success_message()


@step("Acknowledgment​ email should send to the user")
def step_impl(context):
    pass


@then("Should show error message for invalid data type")
def step_impl(context):
    registerUser.verify_error_message()


@then("Submit button should show disabled")
def step_impl(context):
    registerUser.click_on_submit()


@then("Should show error message password and confirmed password not matched")
def step_impl(context):
    pass