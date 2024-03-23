from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.ID, "user_email")
        self.password = (By.ID, "user_password")
        self.submit_btn = (By.NAME, "commit")

    def fill_form_login(self, email, password):
        self.driver.find_element(*self.email).send_keys("tilapia@gmail.com")
        self.driver.find_element(*self.password).send_keys("!Teste123")

    def submit_login(self):
        self.driver.find_element(*self.submit_btn).click()

    def login(self):
        self.driver.get("https://test-bees.herokuapp.com/users/sign_in")
        self.driver.maximize_window()
        self.fill_form_login("tilapia@gmail.com", "!Teste123")
        self.submit_login()

    def is_login_displayed(self):
        login_page_xpath = '/html/body/div/h2'
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page_xpath)))
        login_page = self.driver.find_element(By.XPATH, login_page_xpath)
        assert login_page.is_displayed()
        print('Welcome message displayed')


