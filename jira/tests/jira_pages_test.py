import pytest

from jira.pages.createissue import CreateIssue
from jira.pages.dashboardpage import Dashboard
from jira.pages.loginpage import LoginPage

base_url = "https://jira.hillel.it/secure/Dashboard.jspa"
title = "System Dashboard - Hillel IT School JIRA"
username = "AlexeyGershkovich"
password = "AlexeyGershkovich"
wrong_credentials = "Dummy"
project = "Webinar (WEBINAR)"
issue = "Bug"
summary = "Summary"
long_summary = "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into " \
               "a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his " \
               "brown belly, slightly domed and divided by arches. "


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
        assert Dashboard.is_dashboard_create_issue_button_present(self)


@pytest.mark.usefixtures("driver_init")
class TestDashboardPage:
    def test_create_issue_with_all_required_fields(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, password)
        Dashboard.start_create_issue(self)
        CreateIssue.create_issue(self, project, issue, summary)
        CreateIssue.submit_issue(self)
        assert Dashboard.is_dashboard_avatar_icon_present(self) & Dashboard.is_dashboard_create_issue_button_present(
            self)

    def test_create_issue_with_missing_required_field(self):
        Dashboard.start_create_issue(self)
        CreateIssue.create_issue(self, project, issue, "")
        CreateIssue.submit_issue(self)
        assert CreateIssue.is_error_message_present(self)
        CreateIssue.cancel_creating_issue(self)

    def test_create_issue_with_parameter_text_lenght_longer_than_supported(self):
        Dashboard.start_create_issue(self)
        CreateIssue.create_issue(self, project, issue, long_summary)
        CreateIssue.submit_issue(self)
        assert CreateIssue.is_error_message_present(self)
