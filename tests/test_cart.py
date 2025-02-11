import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_cart_page(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()

    inventory_page = InventoryPage(driver)
    inventory_page.validation_of_inventory_page()

    cart_page = CartPage(driver)
    cart_page.validation_of_cart_page()




