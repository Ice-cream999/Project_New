
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Main_Page(Base):

#LOCATORS
    button_item_1_add_to_card = "//div[@class='inventory_list']/div[1]//button"
    cart = "//span[@class='shopping_cart_badge']"

#GETTERS
    def get_button_item_1_add_to_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_item_1_add_to_card)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

#ACTIONS
    def click_button_item_1_add_to_card(self):
        self.get_button_item_1_add_to_card().click()
        print('Item 1 Added')

    def click_cart(self):
        self.get_cart().click()
        print('Click Cart')

#METHODS
    def add_product(self):
        self.click_button_item_1_add_to_card()
        self.click_cart()
        self.get_current_url()
