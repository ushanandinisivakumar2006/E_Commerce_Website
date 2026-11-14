"""
ProductsPage: Page Object for Product Catalog, Search, Filtering, and Product Details.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class ProductsPage(BasePage):
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BTN = (By.ID, "search-btn")
    CLEAR_SEARCH_BTN = (By.ID, "clear-search-btn")
    RESET_FILTERS_BTN = (By.ID, "reset-filters-btn")
    
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-card")
    PRODUCTS_COUNT_MSG = (By.ID, "products-count-msg")
    NO_PRODUCTS_MSG = (By.ID, "no-products-msg")
    
    SORT_SELECT = (By.ID, "sort-select")
    PRICE_RANGE = (By.ID, "price-range")
    
    # Detail Modal
    DETAIL_MODAL = (By.ID, "product-detail-modal")
    DETAIL_TITLE = (By.XPATH, "//*[@data-testid='detail-title']")
    DETAIL_PRICE = (By.XPATH, "//*[@data-testid='detail-price']")
    DETAIL_QTY_INPUT = (By.ID, "modal-qty-input")
    DETAIL_QTY_PLUS = (By.ID, "modal-qty-plus")
    DETAIL_QTY_MINUS = (By.ID, "modal-qty-minus")
    DETAIL_ADD_CART_BTN = (By.ID, "modal-add-cart-btn")
    CLOSE_DETAIL_BTN = (By.ID, "close-detail-modal-btn")

    def search_product(self, query):
        self.type(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BTN)

    def clear_search(self):
        self.click(self.CLEAR_SEARCH_BTN)

    def filter_by_category(self, category_name):
        locator = (By.XPATH, f"//input[@name='category' and @value='{category_name}']")
        self.click(locator)

    def reset_filters(self):
        self.click(self.RESET_FILTERS_BTN)

    def get_displayed_product_count(self):
        cards = self.find_all(self.PRODUCT_CARDS, timeout=4)
        return len(cards)

    def is_empty_state_visible(self):
        return self.is_visible(self.NO_PRODUCTS_MSG, timeout=3)

    def add_to_cart_by_product_id(self, product_id):
        btn_locator = (By.XPATH, f"//button[@data-testid='add-to-cart-{product_id}']")
        self.click(btn_locator)

    def open_product_details_by_id(self, product_id):
        btn_locator = (By.XPATH, f"//button[@data-testid='view-detail-{product_id}']")
        self.click(btn_locator)
        self.find_visible(self.DETAIL_MODAL)

    def get_detail_modal_title(self):
        return self.get_text(self.DETAIL_TITLE)

    def add_to_cart_from_detail_modal(self):
        self.click(self.DETAIL_ADD_CART_BTN)

    def close_detail_modal(self):
        self.click(self.CLOSE_DETAIL_BTN)
