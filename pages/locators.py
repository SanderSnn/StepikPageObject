from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id=login_form]")
    SIGNUP_FORM = (By.CSS_SELECTOR, "form[id=register_form]")
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, "[id='id_login-username']")
    LOGIN_PASSWORD_FORM = (By.CSS_SELECTOR, "[id='id_login-password']")
    SIGNUP_EMAIL_FORM = (By.CSS_SELECTOR, "[id='id_registration-email']")
    SIGNUP_PASSWORD_FORM = (By.CSS_SELECTOR, "[id='id_registration-password1']")
    SIGNUP_CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR, "[id='id_registration-password2']")
