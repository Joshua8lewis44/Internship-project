from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # You can adjust this wait time as needed

    def click_subscription_link(self):
        try:
            # Try locating the "Subscription & payments" link by text content or class
            # Update the text below to match the actual visible text if needed
            subscription_link = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, "//a[contains(@class, 'page-setting-block') and contains(text(), 'Subscription')]"
                ))
            )

            subscription_link.click()
            print("Successfully clicked the Subscription link.")

        except Exception as e:
            print(f"\nError while trying to click on Subscription link: {e}")
            self.driver.save_screenshot("subscription_link_error.png")
            with open("page_source_dump.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("Saved screenshot and page source for debugging.")
            raise e
