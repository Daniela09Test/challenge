import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


@pytest.mark.usefixtures("driver")
def test_purchase(driver):

    """
    Scenario: Comprar un artículo en SauceDemo
    Given el usuario ha iniciado sesión en SauceDemo
    When el usuario hace clic en el primer artículo de la lista de productos
    Then el primer artículo se agrega al carrito
    When el usuario hace en el botón de carrito de compras
    Then el usuario es redirigido a la página del carrito de compras
    When el usuario hace clic en el botón de finalizar compra
    Then el usuario es redirigido a la página de información del comprador
    When el usuario ingresa la información del comprador requerida
    And el usuario hace  clic en el botón de continuar
    Then el usuario es redirigido a la página de resumen de la compra
    When el usuario hace clic en el botón de finalizar
    Then el usuari es redirigido a la página de confirmación de compra y ve el mensaje de compra exitosa
    """
    # Login
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    # Home page
    home_page = HomePage(driver)
    # Product page
    product_page = ProductPage(driver)
    product_page.click_add_to_cart()
    product_page.click_cart_button()
    # Cart page
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1
    cart_page.click_checkout_button()
    # Checkout step one
    checkout_step_one_page = CheckoutStepOnePage(driver)
    assert checkout_step_one_page.is_page_opened()
    checkout_step_one_page.enter_first_name("Daniela")
    checkout_step_one_page.enter_last_name("Abraham")
    checkout_step_one_page.enter_zip_code("12345")
    checkout_step_one_page.click_continue_button()
    # Checkout step two
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    assert checkout_step_two_page.is_page_opened()
    assert checkout_step_two_page.get_item_total() == "$29.99"
    assert checkout_step_two_page.get_tax() == "$2.40"
    assert checkout_step_two_page.get_total() == "$32.39"
    checkout_step_two_page.click_finish_button()
    # Checkout complete
    checkout_complete_page = CheckoutCompletePage(driver)
    assert checkout_complete_page.get_confirmation_message() == 'Your order has been dispatched, and will arrive just ' \
                                                                'as fast as the pony can get there!'
