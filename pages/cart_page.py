from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    BACKPACK_LINE = (By.ID, "remove-sauce-labs-backpack")
    TSHIRT_LINE = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    BTN_CHECKOUT = (By.ID, 'checkout')


    def check_backpack_line(self):
        assert self.find_element(self.BACKPACK_LINE).is_displayed(), "sauce-labs-backpack item is absent on the cart page"

    def check_tshirt_line(self):
        assert self.find_element(self.TSHIRT_LINE).is_displayed(), "sauce-labs-bolt-t-shirt item is absent on the cart page"

    def click_btn_checkout(self):
        self.click_element(self.BTN_CHECKOUT)

    def validation_of_cart_page(self):
        self.check_backpack_line()
        self.check_tshirt_line()
        self.click_btn_checkout()
        assert "checkout-step-one" in self.driver.current_url, "Ошибка: не совершён переход на страницу checkout-step-one"




