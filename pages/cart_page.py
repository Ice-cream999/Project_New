
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_Page(Base):

#LOCATORS
    button_checkout = "//button[@name='checkout']"
    name_of_product_1 = "//div[@class='cart_list']/div[@class='cart_item'][1]//a"

#GETTERS
    def get_button_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    def get_name_of_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_of_product_1)))

#ACTIONS
    def click_button_checkout(self):
        self.get_button_checkout().click()

#METHODS
    def cart_checout(self):
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.click_button_checkout()
        self.get_screenshot()

