"""
Execute key manual testing scenarios and capture authentic screenshots.
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_evidence_capture():
    os.makedirs("screenshots", exist_ok=True)
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1400,900")
    
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    
    html_file = os.path.abspath("application/index.html")
    app_url = "file:///" + html_file.replace("\\", "/")
    
    print(f"Loading {app_url}...")
    driver.get(app_url)
    time.sleep(1)
    
    # 1. Product Catalog Home
    driver.save_screenshot("screenshots/01-product-catalog.png")
    print("Captured: 01-product-catalog.png")
    
    # 2. Login Modal
    login_nav = driver.find_element(By.ID, "nav-login-btn")
    login_nav.click()
    time.sleep(0.5)
    
    driver.find_element(By.ID, "login-email").send_element = "testuser@example.com"
    email_inp = driver.find_element(By.ID, "login-email")
    email_inp.clear()
    email_inp.send_keys("testuser@example.com")
    pass_inp = driver.find_element(By.ID, "login-password")
    pass_inp.clear()
    pass_inp.send_keys("Password123!")
    time.sleep(0.3)
    driver.save_screenshot("screenshots/02-user-login-modal.png")
    print("Captured: 02-user-login-modal.png")
    
    # 3. User Authenticated
    driver.find_element(By.ID, "login-submit-btn").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/03-user-authenticated.png")
    print("Captured: 03-user-authenticated.png")
    
    # 4. Product Search
    search_input = driver.find_element(By.ID, "search-input")
    search_input.clear()
    search_input.send_keys("Laptop")
    driver.find_element(By.ID, "search-btn").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/04-product-search.png")
    print("Captured: 04-product-search.png")
    
    # Reset search
    driver.find_element(By.ID, "reset-filters-btn").click()
    time.sleep(0.5)
    
    # 5. Category Filter: Electronics
    elec_filter = driver.find_element(By.XPATH, "//input[@name='category' and @value='Electronics']")
    elec_filter.click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/05-category-filter.png")
    print("Captured: 05-category-filter.png")
    
    # 6. Product Details Modal
    driver.find_element(By.XPATH, "//button[@data-testid='view-detail-1']").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/06-product-detail-modal.png")
    print("Captured: 06-product-detail-modal.png")
    
    # Add to cart from modal
    driver.find_element(By.ID, "modal-add-cart-btn").click()
    time.sleep(0.5)
    
    # Also add another product from catalog
    driver.find_element(By.XPATH, "//button[@data-testid='add-to-cart-3']").click()
    time.sleep(0.5)
    
    # 7. Cart Drawer Items
    driver.find_element(By.ID, "cart-toggle-btn").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/07-cart-drawer-items.png")
    print("Captured: 07-cart-drawer-items.png")
    
    # 8. Defect BUG-001: Negative Cart Quantity Input
    driver.execute_script("""
        const el = document.querySelector("[data-testid='cart-qty-input-1']");
        if (el) {
            el.value = "-2";
            el.dispatchEvent(new Event('change'));
        }
    """)
    time.sleep(0.5)
    driver.save_screenshot("screenshots/bug-001-negative-cart-quantity.png")
    print("Captured: bug-001-negative-cart-quantity.png")
    
    # Reset quantity back to 1
    driver.execute_script("""
        const el = document.querySelector("[data-testid='cart-qty-input-1']");
        if (el) {
            el.value = "1";
            el.dispatchEvent(new Event('change'));
        }
    """)
    time.sleep(0.5)
    
    # 9. Checkout Form & Validation
    driver.find_element(By.ID, "proceed-checkout-btn").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/08-checkout-form.png")
    print("Captured: 08-checkout-form.png")
    
    # Clear fields to test empty validation
    driver.find_element(By.ID, "chk-name").clear()
    driver.find_element(By.ID, "chk-email").clear()
    driver.find_element(By.ID, "place-order-btn").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/09-checkout-validation.png")
    print("Captured: 09-checkout-validation.png")
    
    # 10. Defect BUG-002: ZIP Code validation accepting alphabetic chars
    driver.find_element(By.ID, "chk-name").send_keys("Alex Mercer")
    driver.find_element(By.ID, "chk-email").send_keys("alex.mercer@example.com")
    driver.find_element(By.ID, "chk-address").send_keys("742 Evergreen Terrace")
    driver.find_element(By.ID, "chk-city").send_keys("Springfield")
    driver.find_element(By.ID, "chk-state").send_keys("OR")
    driver.find_element(By.ID, "chk-zip").send_keys("ABCDE")
    
    # Select COD
    driver.find_element(By.XPATH, "//input[@name='payment-method' and @value='cod']").click()
    time.sleep(0.3)
    driver.save_screenshot("screenshots/bug-002-zipcode-validation.png")
    print("Captured: bug-002-zipcode-validation.png")
    
    # 11. Complete Order Confirmation
    driver.find_element(By.ID, "place-order-btn").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/10-order-confirmation.png")
    print("Captured: 10-order-confirmation.png")
    
    # Close confirmation
    driver.find_element(By.ID, "conf-continue-shopping-btn").click()
    time.sleep(0.5)
    
    # 12. Defect BUG-003: Search query untrimmed whitespace
    search_input = driver.find_element(By.ID, "search-input")
    search_input.clear()
    search_input.send_keys("  Camera  ")
    driver.find_element(By.ID, "search-btn").click()
    time.sleep(0.5)
    driver.save_screenshot("screenshots/bug-003-search-whitespace.png")
    print("Captured: bug-003-search-whitespace.png")
    
    driver.quit()
    print("All screenshots successfully captured!")

if __name__ == "__main__":
    run_evidence_capture()
