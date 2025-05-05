from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

def browser_init(context):
    """
    Initialize the Firefox WebDriver for Behave tests.
    :param context: Behave context
    """
    # Set up Firefox options
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Optional: Remove this line if you want to see the browser

    # Set up Firefox driver using GeckoDriverManager for automatic driver installation
    driver_path = GeckoDriverManager().install()
    service = Service(driver_path)

    # Initialize the Firefox WebDriver with the service and options
    context.driver = webdriver.Firefox(service=service, options=firefox_options)

    # Optional: Maximize the window and set implicit wait
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)  # Adjust based on your needs

def before_scenario(context, scenario):
    """
    Called before each scenario starts.
    :param context: Behave context
    :param scenario: Current scenario
    """
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)  # Initialize the browser for each scenario

def before_step(context, step):
    """
    Called before each step starts.
    :param context: Behave context
    :param step: Current step
    """
    print('\nStarted step: ', step)

def after_step(context, step):
    """
    Called after each step completes.
    :param context: Behave context
    :param step: Current step
    """
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, scenario):
    """
    Called after each scenario completes.
    :param context: Behave context
    :param scenario: Current scenario
    """
    context.driver.quit()  # Close the browser after each scenario
