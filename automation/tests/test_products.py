"""
Automated Tests: Product Catalog, Search, Filtering, and Product Details.
"""

import pytest
from automation.pages.products_page import ProductsPage

class TestProducts:

    def test_catalog_initial_load(self, driver):
        prod_page = ProductsPage(driver)
        count = prod_page.get_displayed_product_count()
        assert count == 12, f"Expected 12 products on initial load, found {count}"

    def test_search_existing_product(self, driver, test_data):
        prod_page = ProductsPage(driver)
        term = test_data["search"]["valid_term"]
        prod_page.search_product(term)
        
        count = prod_page.get_displayed_product_count()
        assert count >= 1, f"Expected at least 1 product for '{term}', found {count}"

    def test_search_non_existing_product(self, driver, test_data):
        prod_page = ProductsPage(driver)
        term = test_data["search"]["invalid_term"]
        prod_page.search_product(term)
        
        assert prod_page.is_empty_state_visible(), "Empty state message should appear for non-existing products."
        assert prod_page.get_displayed_product_count() == 0

    def test_filter_by_category(self, driver, test_data):
        prod_page = ProductsPage(driver)
        category = test_data["categories"]["electronics"]
        prod_page.filter_by_category(category)
        
        count = prod_page.get_displayed_product_count()
        assert count == 4, f"Expected 4 products in '{category}', found {count}"

    def test_product_detail_modal_opens(self, driver):
        prod_page = ProductsPage(driver)
        prod_page.open_product_details_by_id(1)
        
        title = prod_page.get_detail_modal_title()
        assert "Quantum Pro" in title, f"Expected Quantum Pro details, got '{title}'"
        
        prod_page.close_detail_modal()

