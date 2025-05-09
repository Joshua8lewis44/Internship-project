from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def browser_init(context):
    """
    Initialize the Chrome WebDriver with mobile emulation for Behave tests.
    :param context: Behave context
    """
    # Set up mobile emulation (Nexus 5)
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--headless")  # Optional: remove to see browser UI
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=375,812")  # Mobile-like resolution

    # Set up Chrome driver using ChromeDriverManager
    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set implicit wait
    context.driver.implicitly_wait(4)

def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step:', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step)

def after_scenario(context, scenario):
    context.driver.quit()

