from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_inventory_button = (By.XPATH, '/html/body/div/a')
        self.dropdown_item = (By.XPATH, '//*[@id="inventory_item_id"]')
        self.dropdown_deposit = (By.XPATH, '//*[@id="inventory_deposit_id"]')
        self.item_count = (By.XPATH, '//*[@id="inventory_item_count"]')
        self.create_inventory_button = (By.NAME, 'commit')
        self.inventory_created_message = (By.XPATH, '/html/body/div/p')
        self.show_last_inventory_created = (By.XPATH, '//*[@id="inventories"]/table/tbody/tr[last()]/td[4]/a')
        self.destroy_inventory_button = (By.XPATH, '/html/body/div/div[2]/form/button')
        self.inventory_destroyed_message = (By.XPATH, '/html/body/div/p')

    def create_new_inventory(self):
        self.driver.find_element(*self.new_inventory_button).click()

    def fill_inventory_form(self):
        item_dropdown_element = self.driver.find_element(*self.dropdown_item)
        item_dropdown_element.click()
        item_dropdown = Select(item_dropdown_element)
        item_dropdown.select_by_visible_text("Nao excluir")

        deposit_dropdown_element = self.driver.find_element(*self.dropdown_deposit)
        deposit_dropdown_element.click()
        deposit_dropdown = Select(deposit_dropdown_element)
        deposit_dropdown.select_by_visible_text("Nao excluir")

        self.driver.find_element(*self.item_count).send_keys("100")

    def submit_new_inventory(self):
        self.driver.find_element(*self.create_inventory_button).click()

    def access_the_created_inventory(self):
        self.driver.find_element(*self.show_last_inventory_created).click()

    def destroy_the_inventory(self):
        self.driver.find_element(*self.destroy_inventory_button).click()

    def inventory_destroyed_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.inventory_destroyed_message))
            print('Inventory destroyed message displayed successfully')
            return True
        except TimeoutException:
            print('Inventory destroyed message not displayed within the specified time')
            return False

    def inventory_created_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.inventory_created_message))
            print('Inventory creation message displayed successfully')
            return True
        except TimeoutException:
            print('Inventory creation message not displayed within the specified time')
            return False
