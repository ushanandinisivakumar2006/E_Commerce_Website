"""
LoginPage: Page Object for Login Modal and Authentication interactions.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    NAV_LOGIN_BTN = (By.ID, "nav-login-btn")
    NAV_LOGOUT_BTN = (By.ID, "nav-logout-btn")
    USER_GREETING = (By.ID, "user-greeting")
    
    LOGIN_MODAL = (By.ID, "login-modal")
    LOGIN_EMAIL_INPUT = (By.ID, "login-email")
    LOGIN_PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_SUBMIT_BTN = (By.ID, "login-submit-btn")
    LOGIN_ALERT = (By.ID, "login-alert")
    
    EMAIL_ERROR = (By.ID, "login-email-error")
    PASSWORD_ERROR = (By.ID, "login-password-error")
    CLOSE_MODAL_BTN = (By.ID, "close-login-modal-btn")

    def open_login_modal(self):
        self.click(self.NAV_LOGIN_BTN)
        self.find_visible(self.LOGIN_MODAL)

    def login(self, email, password):
        if email is not None:
            self.type(self.LOGIN_EMAIL_INPUT, email)
        if password is not None:
            self.type(self.LOGIN_PASSWORD_INPUT, password)
        self.click(self.LOGIN_SUBMIT_BTN)

    def get_alert_text(self):
        return self.get_text(self.LOGIN_ALERT)

    def get_email_error(self):
        return self.get_text(self.EMAIL_ERROR)

    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR)

    def is_logged_in(self):
        return self.is_visible(self.USER_GREETING, timeout=3)

    def get_user_greeting(self):
        return self.get_text(self.USER_GREETING)

    def logout(self):
        self.click(self.NAV_LOGOUT_BTN)

