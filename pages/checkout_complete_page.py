"Este archivo contiene los métodos de la página de confirmación de compra"

from selenium.webdriver.common.by import By


class CheckoutCompletePage:
    TITLE_LOCATOR = (By.CLASS_NAME, 'title')
    CONFIRMATION_MESSAGE_LOCATOR = (By.XPATH, '//*[@id="checkout_complete_container"]/div')

    def __init__(self, driver):
        self.driver = driver

    def is_page_opened(self):
        """Verificar si la página de confirmación de compra está abierta"""
        title = self.driver.find_element(*self.TITLE_LOCATOR).text
        return "CHECKOUT: COMPLETE!" in title

    def get_confirmation_message(self):
        """Obtener el mensaje de confirmación de compra"""
        return self.driver.find_element(*self.CONFIRMATION_MESSAGE_LOCATOR).text

