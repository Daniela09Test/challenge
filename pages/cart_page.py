"Este archivo contiene los métodos de la página de carrito de compra"

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        self.page_title = "Swag Labs"
        self.cart_items = self.driver.find_elements(By.XPATH,
                                                    "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]")
        self.checkout_button = (By.ID, 'checkout')

    def click_cart_button(self):
        self.cart_button.click()

    def is_page_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains(self.page_title))
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cart_item")))
            return True
        except:
            return False

    def get_item_count(self):
        return len(self.cart_items)

    def click_checkout_button(self):
        checkout_button = self.driver.find_elements(*self.checkout_button)
        if len(checkout_button) == 1:
            checkout_button[0].click()
        elif len(checkout_button) > 1:
            checkout_button[1].click()
