import pytest

from jira.pages.dashboardpage import Dashboard
from jira.pages.loginpage import LoginPage

base_url = "https://jira.hillel.it/secure/Dashboard.jspa"
title = "System Dashboard - Hillel IT School JIRA"
username = "AlexeyGershkovich"
password = "AlexeyGershkovich"
wrong_credentials = "Dummy"


@pytest.mark.usefixtures("driver_init")
class TestLoginPage:

    def test_open_jira_url(self):
        LoginPage.open_url(self, base_url)
        assert self.driver.title == title

    def test_correct_username_but_wrong_password(self):
        LoginPage.open_url(self, base_url)
        LoginPage.input_username(self, username)
        LoginPage.input_password(self, wrong_credentials)
        LoginPage.submit_credentials(self)
        assert LoginPage.is_error_message_present(self)

    def test_correct_password_but_wrong_username(self):
        LoginPage.open_url(self, base_url)
        LoginPage.input_username(self, wrong_credentials)
        LoginPage.input_password(self, password)
        LoginPage.submit_credentials(self)
        assert LoginPage.is_error_message_present(self)

    def test_correct_username_correct_password(self):
        LoginPage.open_url(self, base_url)
        LoginPage.input_username(self, username)
        LoginPage.input_password(self, password)
        LoginPage.submit_credentials(self)
        assert Dashboard.is_dashboard_avatar_icon_present(self)
