import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("driver")
def test_logout(driver):
    """
    Scenario: Cerrar sesión exitosamente
    Given el usuario ha iniciado sesión en SauceDemo
    When el usuario hace clic en el botón de menú
    And el usuario hace clic en el botón de logout
    Then el usuario debería ver la página de login
    """
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    home_page = HomePage(driver)
    home_page.click_logout_button()
    assert driver.title == "Swag Labs"
