"Este archivo contiene los métodos de la pagina de prooductos"

from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
        self.cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def click_cart_button(self):
        self.cart_button.click()
