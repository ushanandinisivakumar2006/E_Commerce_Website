"""
BasePage: Abstract base class implementing reusable Selenium interactions
and explicit wait wrappers.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []

    def click(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        try:
            wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
        return element

    def type(self, locator, text, clear_first=True, timeout=10):
        element = self.find_visible(locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator, timeout=10):
        element = self.find_visible(locator, timeout)
        return element.text.strip()

    def is_visible(self, locator, timeout=3):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def get_attribute(self, locator, attr, timeout=10):
        element = self.find(locator, timeout)
        return element.get_attribute(attr)

    def execute_js(self, script, *args):
        return self.driver.execute_script(script, *args)
