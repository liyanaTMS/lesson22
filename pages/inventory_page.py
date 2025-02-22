from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")


    def click_on_backpack_btn(self):
        self.click_element(self.BACKPACK_BTN)

    def click_on_tshirt_btn(self):
        self.click_element(self.TSHIRT_BTN)

    def click_on_cart_icon(self):
        self.click_element(self.CART_ICON)

    def validation_of_inventory_page(self):
        self.click_on_backpack_btn()
        self.click_on_tshirt_btn()
        self.click_on_cart_icon()
        assert "cart" in self.driver.current_url, "Ошибка: не совершён переход в корзину"



