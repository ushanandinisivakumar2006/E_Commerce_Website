"""
Pytest configuration, driver fixtures, and failure screenshot hooks.
"""

import os
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def test_data():
    data_path = os.path.join(os.path.dirname(__file__), "test_data", "test_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,900")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    
    # Path to local e-commerce demo application
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "application"))
    index_file = os.path.join(base_dir, "index.html")
    app_url = "file:///" + index_file.replace("\\", "/")
    
    driver.get(app_url)
    
    yield driver
    
    # Teardown
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = os.path.join(os.path.dirname(__file__), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_file = os.path.join(screenshot_dir, f"{item.name}_failed.png")
            driver.save_screenshot(screenshot_file)
            
            # Attach to pytest-html if available
            try:
                import pytest_html
                extras.append(pytest_html.extras.image(screenshot_file))
                report.extras = extras
            except Exception:
                pass
