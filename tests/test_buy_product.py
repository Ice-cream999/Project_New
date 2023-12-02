import time

from selenium import webdriver
from pages.login_page import Login_Page
from pages.main_page import Main_Page
from pages.cart_page import Cart_Page


def test_buy_product():
    driver = webdriver.Chrome()

    print('Start Test')

    lp = Login_Page(driver)
    lp.authorization()

    mp = Main_Page(driver)
    mp.add_product()

    cp = Cart_Page(driver)
    cp.cart_checout()

    time.sleep(2)
    driver.quit()



