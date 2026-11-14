"""
Automated Tests: Checkout Form Validation and Order Confirmation.
"""

import pytest
from automation.pages.products_page import ProductsPage
from automation.pages.cart_page import CartPage
from automation.pages.checkout_page import CheckoutPage

class TestCheckout:

    def test_checkout_form_empty_validation(self, driver):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        chk_page = CheckoutPage(driver)
        
        prod_page.add_to_cart_by_product_id(1)
        cart_page.open_cart()
        cart_page.proceed_to_checkout()
        
        chk_page.submit_order()
        
        assert "Full name is required" in chk_page.get_name_error()
        assert "Email address is required" in chk_page.get_email_error()

    def test_checkout_form_invalid_email(self, driver, test_data):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        chk_page = CheckoutPage(driver)
        
        prod_page.add_to_cart_by_product_id(1)
        cart_page.open_cart()
        cart_page.proceed_to_checkout()
        
        chk_page.fill_shipping_info(
            name="John Doe",
            email="invalid-email",
            address="123 Test St",
            city="Seattle",
            state="WA",
            zip_code="98101"
        )
        chk_page.submit_order()
        
        assert "valid email" in chk_page.get_email_error().lower()

    def test_successful_order_placement_cod(self, driver, test_data):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        chk_page = CheckoutPage(driver)
        
        shipping = test_data["checkout"]["valid_shipping"]
        
        prod_page.add_to_cart_by_product_id(1)
        cart_page.open_cart()
        cart_page.proceed_to_checkout()
        
        chk_page.fill_shipping_info(
            name=shipping["name"],
            email=shipping["email"],
            address=shipping["address"],
            city=shipping["city"],
            state=shipping["state"],
            zip_code=shipping["zip"]
        )
        chk_page.select_payment_method("cod")
        chk_page.submit_order()
        
        assert chk_page.is_confirmation_visible(), "Order confirmation modal was not displayed."
        order_id = chk_page.get_order_id()
        assert order_id.startswith("ORD-"), f"Expected order ID format ORD-XXXXXX, got '{order_id}'"

    def test_cart_cleared_post_order(self, driver, test_data):
        prod_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        chk_page = CheckoutPage(driver)
        
        shipping = test_data["checkout"]["valid_shipping"]
        
        prod_page.add_to_cart_by_product_id(1)
        cart_page.open_cart()
        cart_page.proceed_to_checkout()
        
        chk_page.fill_shipping_info(
            name=shipping["name"],
            email=shipping["email"],
            address=shipping["address"],
            city=shipping["city"],
            state=shipping["state"],
            zip_code=shipping["zip"]
        )
        chk_page.select_payment_method("cod")
        chk_page.submit_order()
        chk_page.continue_shopping()
        
        # Verify cart badge reset
        assert cart_page.get_badge_count() == 0, "Cart badge was not reset after order placement."
