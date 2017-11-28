from time import sleep
from selenium import webdriver
from os import path
from unittest import TestCase
import os


test =  TestCase()

class RegisterUser():

    def __init__(self):
        dir = os.path.dirname(__file__)
        chrome_driver_path = path.join(dir, '../chromedriver')
        self.driver = webdriver.Chrome(chrome_driver_path)


    def user_navigation(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://bit.ly/dxqatest-online")


    def set_required_fields_data(self,params):
        self.set_first_name(params['first_name'])
        self.set_last_name(params['last_name'])
        self.set_username(params['username'])
        self.set_password(params['password'])
        self.set_confirm_password(params['confirm_password'])
        self.set_email_id(params['email_id'])



    def set_optional_fields_data(self,params):
        self.set_department(params['Department'])
        self.set_contact_no(params['contact_no'])





    def set_first_name(self,first_name):
        self.driver.find_element_by_name("first_name").send_keys(first_name)

    def set_last_name(self,last_name):
        self.driver.find_element_by_name("last_name").send_keys(last_name)

    def set_department(self,Department):
        departments = self.driver.find_elements_by_css_selector(".selectpicker option")
        for dept in departments[1:]:
            if Department == dept.text:
                dept.click()



    def set_username(self,username):
        self.driver.find_element_by_name("user_name").send_keys(username)

    def set_password(self,password):
        self.driver.find_element_by_name("user_password").send_keys(password)

    def set_confirm_password(self,confirm_password):
        self.driver.find_element_by_name("confirm_password").send_keys(confirm_password)

    def set_email_id(self,email_id):
        self.driver.find_element_by_name("email").send_keys(email_id)


    def set_contact_no(self,contact_no):
        self.driver.find_element_by_name("contact_no").send_keys(contact_no)



    def click_on_submit(self):
        submit = self.driver.find_element_by_class_name("btn-warning")
        if submit.is_enabled():
            submit.click()





    def verify_success_message(self):
        message = self.driver.find_element_by_id("contact_form")
        test.assertEqual(message.text,"Thanks","Message showing correctly")


    def verify_error_message(self):
        error_message = self.driver.find_element_by_class_name("help-block")

        test.assertEqual(error_message.text,"This value is not valid")
        # if error_message.text == "This value is not valid":
        #     print("Error message should be user friendly")















    def tearDown(self):
        self.driver.close()








