from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[1]/div/div/input")
    PASSWORD_FIELD = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/input")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary') and contains(., 'LogIn')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(normalize-space(text()), 'User Logged In Successfully')]")
    PROJECT_TAB = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/a[2]/div/p")
    PROJECT_TAB_CONTENT = (By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div/div[1]/div")