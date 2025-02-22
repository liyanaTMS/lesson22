import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_page(driver):
    """Тестирует EndToEnd сценарий проверки работы"Checkout Step One" страницы"""
    login_page = LoginPage(driver)
    login_page.valid_login()

    inventory_page = InventoryPage(driver)
    inventory_page.validation_of_inventory_page()

    cart_page = CartPage(driver)
    cart_page.validation_of_cart_page()

    # Проверка наличия на странице инфо-лейбла, враппера "FirstName, LastName, PostalCode", кнопки "Continue"
    checkout_page = CheckoutPage(driver)
    checkout_page.check_info()
    checkout_page.check_wrapper()
    checkout_page.check_btn_continue()

    # Ввод полей "FirstName, LastName, PostalCode", нажатие кнопки "Continue"
    checkout_page.enter_firstname("Ivan")
    checkout_page.enter_lastname("Ivanov")
    checkout_page.enter_post("222222")
    checkout_page.click_btn_continue()
    assert "checkout-step-two" in driver.current_url, "Ошибка: не совершён переход на страницу checkout-step-two"


