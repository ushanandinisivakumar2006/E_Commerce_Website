"""
CartPage: Page Object for Shopping Cart Drawer and Quantity adjustments.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class CartPage(BasePage):
    CART_TOGGLE_BTN = (By.ID, "cart-toggle-btn")
    CART_BADGE = (By.ID, "cart-badge")
    CART_DRAWER = (By.ID, "cart-drawer")
    CLOSE_CART_BTN = (By.ID, "close-cart-btn")
    
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item")
    CART_SUBTOTAL = (By.ID, "cart-subtotal")
    CART_TAX = (By.ID, "cart-tax")
    CART_TOTAL = (By.ID, "cart-total")
    
    CLEAR_CART_BTN = (By.ID, "clear-cart-btn")
    PROCEED_CHECKOUT_BTN = (By.ID, "proceed-checkout-btn")
    CART_EMPTY_STATE = (By.CSS_SELECTOR, ".cart-empty-state")

    def open_cart(self):
        self.click(self.CART_TOGGLE_BTN)
        self.find_visible(self.CART_DRAWER)

    def close_cart(self):
        self.click(self.CLOSE_CART_BTN)

    def get_badge_count(self):
        text = self.get_text(self.CART_BADGE)
        return int(text) if text.isdigit() else 0

    def get_cart_items_count(self):
        return len(self.find_all(self.CART_ITEMS, timeout=3))

    def increment_item_quantity(self, product_id):
        plus_btn = (By.XPATH, f"//button[@data-testid='cart-qty-plus-{product_id}']")
        self.click(plus_btn)

    def decrement_item_quantity(self, product_id):
        minus_btn = (By.XPATH, f"//button[@data-testid='cart-qty-minus-{product_id}']")
        self.click(minus_btn)

    def remove_item(self, product_id):
        remove_btn = (By.XPATH, f"//button[@data-testid='cart-remove-btn-{product_id}']")
        self.click(remove_btn)

    def clear_cart(self):
        self.click(self.CLEAR_CART_BTN)

    def get_subtotal(self):
        return self.get_text(self.CART_SUBTOTAL)

    def get_tax(self):
        return self.get_text(self.CART_TAX)

    def get_total(self):
        return self.get_text(self.CART_TOTAL)

    def proceed_to_checkout(self):
        self.click(self.PROCEED_CHECKOUT_BTN)

    def is_cart_empty(self):
        return self.is_visible(self.CART_EMPTY_STATE, timeout=3)
