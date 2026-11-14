"""
CheckoutPage: Page Object for Checkout Form, Validation, and Order Confirmation.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_MODAL = (By.ID, "checkout-modal")
    CLOSE_CHECKOUT_BTN = (By.ID, "close-checkout-modal-btn")
    PLACE_ORDER_BTN = (By.ID, "place-order-btn")
    
    # Form Fields
    CHK_NAME = (By.ID, "chk-name")
    CHK_EMAIL = (By.ID, "chk-email")
    CHK_ADDRESS = (By.ID, "chk-address")
    CHK_CITY = (By.ID, "chk-city")
    CHK_STATE = (By.ID, "chk-state")
    CHK_ZIP = (By.ID, "chk-zip")
    
    NAME_ERROR = (By.ID, "chk-name-error")
    EMAIL_ERROR = (By.ID, "chk-email-error")
    ADDRESS_ERROR = (By.ID, "chk-address-error")
    CITY_ERROR = (By.ID, "chk-city-error")
    STATE_ERROR = (By.ID, "chk-state-error")
    ZIP_ERROR = (By.ID, "chk-zip-error")
    
    PAY_COD_RADIO = (By.XPATH, "//input[@name='payment-method' and @value='cod']")
    PAY_CREDIT_RADIO = (By.XPATH, "//input[@name='payment-method' and @value='credit']")
    
    CARD_NUMBER = (By.ID, "chk-card-number")
    CARD_EXP = (By.ID, "chk-card-exp")
    CARD_CVV = (By.ID, "chk-card-cvv")
    
    # Confirmation Modal
    CONF_MODAL = (By.ID, "confirmation-modal")
    CONF_ORDER_ID = (By.ID, "conf-order-id")
    CONF_TOTAL = (By.ID, "conf-total")
    CONF_CONTINUE_BTN = (By.ID, "conf-continue-shopping-btn")

    def fill_shipping_info(self, name="", email="", address="", city="", state="", zip_code=""):
        if name:
            self.type(self.CHK_NAME, name)
        if email:
            self.type(self.CHK_EMAIL, email)
        if address:
            self.type(self.CHK_ADDRESS, address)
        if city:
            self.type(self.CHK_CITY, city)
        if state:
            self.type(self.CHK_STATE, state)
        if zip_code:
            self.type(self.CHK_ZIP, zip_code)

    def select_payment_method(self, method="cod"):
        if method == "cod":
            self.click(self.PAY_COD_RADIO)
        else:
            self.click(self.PAY_CREDIT_RADIO)

    def submit_order(self):
        self.click(self.PLACE_ORDER_BTN)

    def get_name_error(self):
        return self.get_text(self.NAME_ERROR)

    def get_email_error(self):
        return self.get_text(self.EMAIL_ERROR)

    def is_confirmation_visible(self):
        return self.is_visible(self.CONF_MODAL, timeout=4)

    def get_order_id(self):
        return self.get_text(self.CONF_ORDER_ID)

    def continue_shopping(self):
        self.click(self.CONF_CONTINUE_BTN)
