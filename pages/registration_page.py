from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.ID, "user_email")
        self.password = (By.ID, "user_password")
        self.confirm_password = (By.ID, "user_password_confirmation")
        self.submit_btn = (By.NAME, "commit")

    def fill_form(self, email, password, confirm_password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)

    def submit_registration(self):
        self.driver.find_element(*self.submit_btn).click()
