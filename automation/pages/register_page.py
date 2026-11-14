"""
RegisterPage: Page Object for User Registration modal.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class RegisterPage(BasePage):
    NAV_REGISTER_BTN = (By.ID, "nav-register-btn")
    REGISTER_MODAL = (By.ID, "register-modal")
    REG_NAME = (By.ID, "reg-name")
    REG_EMAIL = (By.ID, "reg-email")
    REG_PASSWORD = (By.ID, "reg-password")
    REG_CONFIRM_PASSWORD = (By.ID, "reg-confirm-password")
    REG_SUBMIT_BTN = (By.ID, "register-submit-btn")
    REG_ALERT = (By.ID, "register-alert")

    NAME_ERROR = (By.ID, "reg-name-error")
    EMAIL_ERROR = (By.ID, "reg-email-error")
    PASSWORD_ERROR = (By.ID, "reg-password-error")
    CONFIRM_PASSWORD_ERROR = (By.ID, "reg-confirm-password-error")

    def open_register_modal(self):
        self.click(self.NAV_REGISTER_BTN)
        self.find_visible(self.REGISTER_MODAL)

    def register(self, name, email, password, confirm_password):
        if name:
            self.type(self.REG_NAME, name)
        if email:
            self.type(self.REG_EMAIL, email)
        if password:
            self.type(self.REG_PASSWORD, password)
        if confirm_password:
            self.type(self.REG_CONFIRM_PASSWORD, confirm_password)
        self.click(self.REG_SUBMIT_BTN)

    def get_alert_text(self):
        return self.get_text(self.REG_ALERT)

    def get_name_error(self):
        return self.get_text(self.NAME_ERROR)

    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR)
