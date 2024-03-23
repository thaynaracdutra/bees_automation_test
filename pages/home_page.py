from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.XPATH, '/html/body/div/p')
        self.deposits_button = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a')
        self.items_button = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
        self.inventory_button = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a')
        self.logout_button = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/form/button')

    def go_to_deposits_page(self):
        self.driver.find_element(*self.deposits_button).click()

    def go_to_items_page(self):
        self.driver.find_element(*self.items_button).click()

    def go_to_inventory_page(self):
        self.driver.find_element(*self.inventory_button).click()

    def logout(self):
        self.driver.find_element(*self.logout_button).click()

    def is_welcome_message_displayed(self):
        welcome_message_xpath = '/html/body/div/p'
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, welcome_message_xpath)))
        welcome_message = self.driver.find_element(By.XPATH, welcome_message_xpath)
        assert welcome_message.is_displayed()
        print('Welcome message displayed')
