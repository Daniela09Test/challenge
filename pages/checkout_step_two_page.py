"Este archivo contiene los métodos del segundo paso para realizar el pago de la compra"

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = self.driver.find_element(By.XPATH, '//button[@id="finish"]')

    def get_item_total(self):
        item_total_element = self.driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
        return item_total_element.text.split(": ")[1]

    def get_tax(self):
        item_taxt = self.driver.find_element(By.XPATH, "//div[@class='summary_tax_label']")
        return item_taxt.text.split(": ")[1]

    def get_total(self):
        item_total = self.driver.find_element(By.CSS_SELECTOR, "div.page_wrapper div:nth-child(1) div.checkout_summary_container div:nth-child(1) div.summary_info > div.summary_info_label.summary_total_label:nth-child(8)")
        return item_total.text.split(": ")[1]

    def click_finish_button(self):
        self.finish_button.click()

    def is_page_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("Swag Labs"))
            return True
        except TimeoutException:
            return False
