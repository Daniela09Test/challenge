"Este archivo contiene los métodos del menu hamburguesa"

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
        self.logout_button = driver.find_element(By.ID, 'logout_sidebar_link')

    def click_menu_button(self):
        self.menu_button.click()

    def click_logout_button(self):
        self.click_menu_button()
        self.logout_button.click()
