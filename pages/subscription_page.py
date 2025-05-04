from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds max

    def is_page_title_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Subscription & payments')]"))
        ).is_displayed()

    def is_back_button_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), '<- Back')]"))
        ).is_displayed()

    def is_upgrade_button_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Upgrade plan']"))
        ).is_displayed()
