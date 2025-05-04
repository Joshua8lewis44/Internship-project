from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_settings(self):
        self.driver.find_element(By.XPATH, "//div[text()='Settings']").click()
