import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_locked_user_login(driver):
    """Тестирует вход locked_user-а на сайт https://www.saucedemo.com/"""
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()
    # Проверка появления красного сообщения об ошибке "Sorry, this user has been locked out."
    message_error = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
    assert message_error == "Epic sadface: Sorry, this user has been locked out."