from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ItemsPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_item = (By.XPATH, '/html/body/div/a')
        self.item_name_field = (By.XPATH, '//*[@id="item_name"]')
        self.item_height_field = (By.XPATH, '//*[@id="item_height"]')
        self.item_width_field = (By.XPATH, '//*[@id="item_width"]')
        self.item_weight_field = (By.XPATH, '//*[@id="item_weight"]')
        self.create_item_button = (By.NAME, 'commit')
        self.item_created_message = (By.XPATH, '/html/body/div/p')

    def create_new_item(self):
        self.driver.find_element(*self.new_item).click()

    def fill_item_form(self):
        self.driver.find_element(*self.item_name_field).send_keys("Zúleide")
        self.driver.find_element(*self.item_height_field).send_keys("0.8")
        self.driver.find_element(*self.item_width_field).send_keys("0.8")
        self.driver.find_element(*self.item_weight_field).send_keys("0.8")

    def submit_new_item(self):
        self.driver.find_element(*self.create_item_button).click()

    def item_created_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.item_created_message))
            print('Deposit was successfully created message displayed')
            return True
        except TimeoutException:
            print('Deposit creation message not displayed within the specified time')
            return False
