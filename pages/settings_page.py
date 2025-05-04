from selenium.webdriver.common.by import By

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_subscription_link(self):
        self.driver.find_element(By.XPATH, "//div[text()='Subscription & payments']").click()
