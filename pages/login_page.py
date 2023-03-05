"Este archivo contiene los métodos del acceso a la aplicación"

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        if not isinstance(driver, webdriver.Chrome):
            raise ValueError("Expected a Chrome WebDriver")
        self.driver = driver
        self.username_input = driver.find_element(By.ID, 'user-name' )
        self.password_input = driver.find_element(By.ID, 'password')
        self.login_button = driver.find_element(By.ID, 'login-button')

    def enter_username(self, username):
        self.username_input.clear()
        self.username_input.send_keys(username)

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def click_login_button(self):
        self.login_button.click()