from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
#from locators.locators import LoginPageLocators  # Correct import path
from locators.locactors import LoginPageLocators

# Define the path to ChromeDriver
service = Service("D:\\Dileep_project\\chromedriver\\chromedriver.exe")  # Ensure correct path

@given('I open the login page')
def step_impl(context):
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://hrdurapid.azurewebsites.net/")
    context.driver.maximize_window()
    sleep(5)

@when('I enter username and password')
def step_impl(context):
    context.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("dileep.durapid@outlook.com")  # Replace with your actual username
    context.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("dileep12")  # Replace with your actual password

@when('I click on the login button')
def step_impl(context):
    context.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    sleep(10)

@then('I should see a successful login message')
def step_impl(context):
    success_message = context.driver.find_element(*SUCCESS_MESSAGE)
    assert success_message.is_displayed(), "Login success message is not displayed"
    assert success_message.text == "User Logged In Successfully", "Unexpected login success message text"

sleep(10)
@when("I click on the project tab")
def step_click_project_tab(context):
    # Locate and click the Project Tab button
    project_tab = context.driver.find_element(*LoginPageLocators.PROJECT_TAB)
    project_tab.click()

    sleep(10)

@then("I should see the project tab open successfully")
def step_verify_project_tab(context):
    # Verify that the Project Tab content is displayed
    project_tab_content = context.driver.find_element(**LoginPageLocators.PROJECT_TAB_CONTENT)
    assert project_tab_content.is_displayed(), "Project tab did not open successfully"
