from selenium import webdriver
from random import randint
from web_urls import registration_page, login_page

pass_value = randint(10**(5-1), (10**5)-1)
mail_random = randint(10**(5-1), (10**5)-1)
mail_address = str(mail_random) + '@gmail.com'

class Application:

    def __init__(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def add_client(self):
        self.browser.get(registration_page)
        email_field = self.browser.find_element_by_id('reg_username')
        email_field.send_keys(mail_address)
        pass_field = self.browser.find_element_by_id('reg_pass1')
        pass_field.send_keys(pass_value)
        confirm_pass_field = self.browser.find_element_by_id('reg_pass2')
        confirm_pass_field.send_keys(pass_value)
        send_button = self.browser.find_element_by_id('register')
        send_button.click()

    def login_as_client(self):
        self.browser.get(login_page)
        mail_value = self.browser.find_element_by_id('username')
        mail_value.send_keys(mail_address)
        password_field = self.browser.find_element_by_id('password')
        password_field.send_keys(pass_value)
        login_button = self.browser.find_element_by_id('login')
        login_button.click()

    def destroy(self):
        self.browser.quit()
