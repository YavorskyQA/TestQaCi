import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_success(driver):
    driver.get("https://my.proweb.uz/log-in")

    login = LoginPage(driver)
    login.enter_phone_number("998946871551")
    login.click_login()
    login.enter_password("6871551darkshin")
    login.click_login()
    login.find_dropdown()
    login.click_btn_finish()

    # home_page = HomePage(driver)
    # home_page.click_profile()
    # home_page.click_exit()
    # home_page.click_sure_exit()
    home_page.click_qa()
    home_page.click_ranks()
    home_page.click_homework()
    home_page.select_hw()



# def test_login_invalid(driver):
#     driver.get("https://my.proweb.uz/log-in")
#
#     login = LoginPage(driver)
#     login.enter_phone_number("998947856556")
#     login.click_login()
#     login.enter_password("6544684")
#     login.click_login()
