import pytest
from pages.login_page import LoginPage

def test_positive_login_scenario(driver):
    """Тестирует позитивный сценарий входа на сайт https://www.saucedemo.com/"""
    login_page = LoginPage(driver)
    login_page.valid_login()