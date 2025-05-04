from behave import given, when, then
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.subscription_page import SubscriptionPage

@given("the user is on the main page and already logged in")
def step_impl(context):
    context.driver.get("https://soft.reelly.io")

@when("the user navigates to the Subscription & payments page")
def step_impl(context):
    MainPage(context.driver).click_settings()
    SettingsPage(context.driver).click_subscription_link()

@then("the Subscription & payments page should be displayed")
def step_impl(context):
    assert SubscriptionPage(context.driver).is_page_title_visible()

@then('the "Back" and "Upgrade Plan" buttons should be visible')
def step_impl(context):
    page = SubscriptionPage(context.driver)
    assert page.is_back_button_visible()
    assert page.is_upgrade_button_visible()
