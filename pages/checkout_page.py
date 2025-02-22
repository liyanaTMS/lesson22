from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_INFO = (By.CLASS_NAME, "title")
    CHECKOUT_WRAPPER = (By.CLASS_NAME, "checkout_info")
    BTN_CONTINUE = (By.ID, "continue")
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    POST_INPUT = (By.ID, "postal-code")


    def check_info(self):
        info_label = self.find_element(self.CHECKOUT_INFO)
        assert info_label.text == "Checkout: Your Information", "Checkout information label is absent"


    def check_btn_continue(self):
        btn_continue = self.find_element(self.BTN_CONTINUE)
        assert btn_continue.is_displayed(), "Button Continue is absent"


    def check_wrapper(self):
        checkout_wrapper = self.find_element(self.CHECKOUT_WRAPPER)
        assert checkout_wrapper.is_displayed(), "Checkout wrapper is absent"


    def enter_firstname(self, firstname):
        self.enter_text(self.FIRSTNAME_INPUT, firstname)

    def enter_lastname(self, lastname):
        self.enter_text(self.LASTNAME_INPUT, lastname)

    def enter_post(self, postal_code):
        self.enter_text(self.POST_INPUT, postal_code)

    def click_btn_continue(self):
        self.click_element(self.BTN_CONTINUE)