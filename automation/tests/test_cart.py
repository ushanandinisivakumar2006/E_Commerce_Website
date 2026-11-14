"""
Automated Tests: Shopping Cart (Add, Update Quantity, Remove, Clear).
"""

import pytest
from automation.pages.products_page import ProductsPage
from automation.pages.cart_page import CartPage

class TestCart:

    def test_add_to_cart_from_catalog(self, driver):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        
        initial_badge = cart_page.get_badge_count()
        assert initial_badge == 0
        
        prod_page.add_to_cart_by_product_id(1)
        
        updated_badge = cart_page.get_badge_count()
        assert updated_badge == 1, f"Expected badge count 1, got {updated_badge}"

    def test_cart_drawer_display(self, driver):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        
        prod_page.add_to_cart_by_product_id(1)
        cart_page.open_cart()
        
        items_count = cart_page.get_cart_items_count()
        assert items_count == 1, f"Expected 1 item in cart drawer, got {items_count}"
        assert "$199.99" in cart_page.get_subtotal()

    def test_increment_quantity(self, driver):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        
        prod_page.add_to_cart_by_product_id(1)
        cart_page.open_cart()
        cart_page.increment_item_quantity(1)
        
        updated_badge = cart_page.get_badge_count()
        assert updated_badge == 2, f"Expected badge count 2 after increment, got {updated_badge}"
        assert "$399.98" in cart_page.get_subtotal()

    def test_remove_product_from_cart(self, driver):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        
        prod_page.add_to_cart_by_product_id(1)
        prod_page.add_to_cart_by_product_id(3)
        
        cart_page.open_cart()
        assert cart_page.get_cart_items_count() == 2
        
        cart_page.remove_item(1)
        assert cart_page.get_cart_items_count() == 1

    def test_clear_entire_cart(self, driver):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        
        prod_page.add_to_cart_by_product_id(1)
        cart_page.open_cart()
        cart_page.clear_cart()
        
        assert cart_page.is_cart_empty(), "Cart should display empty state after clearing."
        assert cart_page.get_badge_count() == 0

