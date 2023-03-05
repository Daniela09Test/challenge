"Este archivo contiene los métodos del primer paso para realizar el pago de la compra"

from selenium.webdriver.common.by import By


class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = self.driver.find_element(By.ID, 'first-name')
        self.last_name_input = self.driver.find_element(By.ID, 'last-name')
        self.zip_code_input = self.driver.find_element(By.ID, 'postal-code')
        self.continue_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        self.header = driver.find_element(By.CLASS_NAME, 'header_secondary_container')

    def enter_first_name(self, first_name):
        self.first_name_input.clear()
        self.first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        self.last_name_input.clear()
        self.last_name_input.send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.zip_code_input.clear()
        self.zip_code_input.send_keys(zip_code)

    def click_continue_button(self):
        self.continue_button.click()

    def is_page_opened(self):
        return "checkout-step-one" in self.driver.current_url and self.header.is_displayed()
