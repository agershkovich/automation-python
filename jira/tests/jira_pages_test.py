from time import sleep

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
        LoginPage.login_to_jira(self, username, wrong_credentials)
        assert LoginPage.is_error_message_present(self)

    def test_correct_password_but_wrong_username(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, wrong_credentials, password)
        assert LoginPage.is_error_message_present(self)

    def test_correct_username_correct_password(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, password)
        assert Dashboard.is_dashboard_avatar_icon_present(self)


@pytest.mark.usefixtures("driver_init")
class TestDashboardPage:
    def test_create_issue_with_all_required_fields(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, password)
        Dashboard.start_create_issue(self)
