"""
Automated Tests: User Authentication (Login, Validation, Logout).
"""

import pytest
from automation.pages.login_page import LoginPage

class TestAuthentication:

    def test_valid_user_login(self, driver, test_data):
        login_page = LoginPage(driver)
        user = test_data["users"]["valid_user"]
        
        login_page.open_login_modal()
        login_page.login(user["email"], user["password"])
        
        assert login_page.is_logged_in(), "User profile greeting was not visible after valid login."
        assert "Test User" in login_page.get_user_greeting()

    def test_invalid_password_login(self, driver, test_data):
        login_page = LoginPage(driver)
        user = test_data["users"]["invalid_password_user"]
        
        login_page.open_login_modal()
        login_page.login(user["email"], user["password"])
        
        alert_msg = login_page.get_alert_text()
        assert "Incorrect password" in alert_msg, f"Expected password error alert, got '{alert_msg}'"
        assert not login_page.is_logged_in(), "User should not be logged in with incorrect password."

    def test_unregistered_email_login(self, driver, test_data):
        login_page = LoginPage(driver)
        user = test_data["users"]["non_existent_user"]
        
        login_page.open_login_modal()
        login_page.login(user["email"], user["password"])
        
        alert_msg = login_page.get_alert_text()
        assert "User does not exist" in alert_msg, f"Expected non-existent user error, got '{alert_msg}'"

    def test_empty_login_validation(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_modal()
        login_page.login("", "")
        
        assert "Email address is required" in login_page.get_email_error()
        assert "Password is required" in login_page.get_password_error()

    def test_user_logout(self, driver, test_data):
        login_page = LoginPage(driver)
        user = test_data["users"]["valid_user"]
        
        login_page.open_login_modal()
        login_page.login(user["email"], user["password"])
        assert login_page.is_logged_in()
        
        login_page.logout()
        assert not login_page.is_logged_in(), "User should be logged out after clicking Logout."

