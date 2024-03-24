from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DepositsPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_deposit_button = (By.XPATH, '/html/body/div/a')
        self.deposit_name_field = (By.XPATH, '//*[@id="deposit_name"]')
        self.deposit_address_field = (By.XPATH, '//*[@id="deposit_address"]')
        self.deposit_city_field = (By.XPATH, '//*[@id="deposit_city"]')
        self.deposit_state_field = (By.XPATH, '//*[@id="deposit_state"]')
        self.deposit_zipcode_field = (By.XPATH, '//*[@id="deposit_zipcode"]')
        self.create_deposit_button = (By.NAME, 'commit')
        self.deposit_created_message = (By.XPATH, '/html/body/div/p')

    def create_new_deposit(self):
        self.driver.find_element(*self.new_deposit_button).click()

    def fill_deposit_form(self, name, address, city, state, zipcode):
        self.driver.find_element(*self.deposit_name_field).send_keys(name)
        self.driver.find_element(*self.deposit_address_field).send_keys(address)
        self.driver.find_element(*self.deposit_city_field).send_keys(city)
        self.driver.find_element(*self.deposit_state_field).send_keys(state)

    def submit_new_deposit(self):
        self.driver.find_element(*self.create_deposit_button).click()

    def deposit_created_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.deposit_created_message))
            print('Deposit was successfully created message displayed')
            return True
        except TimeoutException:
            print('Deposit creation message not displayed within the specified time')
            return False

