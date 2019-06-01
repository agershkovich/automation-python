import allure
import pytest

from jira.api.jira_api_actions import ApiInteractions as API
from jira.pages.createissue import CreateIssue
from jira.pages.dashboardpage import Dashboard
from jira.pages.loginpage import LoginPage
from jira.pages.myopenissues import MyOpenIssues
from jira.pages.searchpage import SearchPage

base_url = "https://jira.hillel.it/secure/Dashboard.jspa"
base_url_api = "https://jira.hillel.it"
title = "System Dashboard - Hillel IT School JIRA"
username = "AlexeyGershkovich"
password = "AlexeyGershkovich"
authorization = "Basic QWxleGV5R2Vyc2hrb3ZpY2g6QWxleGV5R2Vyc2hrb3ZpY2g="
wrong_credentials = "Dummy"
project = "WEBINAR"
issue = "Bug"
priority = "High"

long_summary = "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into " \
               "a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his " \
               "brown belly, slightly domed and divided by arches. "

keywords = "Not result"
original_estimate = "3w 4d 12h"
remaining_estimate = "5w 1d 8h"

create_issue_endpoint = base_url_api + "/rest/api/2/issue"
search_issue_endpoint = base_url_api + "/rest/api/2/search"
modify_issue_endpoint = base_url_api + "/rest/api/2/issue/{0}"

headers = {
    "Authorization": authorization,
    "Content-Type": "application/json"
}


@pytest.mark.usefixtures("driver_init")
class TestLoginPage:
    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Login to Jira")
    def test_open_jira_url(self):
        LoginPage.open_url(self, base_url)
        assert self.driver.title == title

    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Login to Jira using correct username but wrong password")
    def test_correct_username_but_wrong_password(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, wrong_credentials)
        assert LoginPage.is_error_message_present(self)

    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Login to Jira using correct password but wrong username")
    def test_correct_password_but_wrong_username(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, wrong_credentials, password)
        assert LoginPage.is_error_message_present(self)

    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Login to Jira using correct username and password")
    def test_correct_username_correct_password(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, password)
        assert Dashboard.is_dashboard_create_issue_button_present(self)


@pytest.mark.usefixtures("driver_init")
class TestCreateIssue:
    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Create an issue with all required fields")
    def test_create_issue_with_all_required_fields(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, password)
        Dashboard.start_create_issue(self)
        CreateIssue.create_issue(self, project, issue, CreateIssue.summary, original_estimate, remaining_estimate)
        CreateIssue.submit_issue(self)
        assert Dashboard.is_dashboard_avatar_icon_present(self) & Dashboard.is_dashboard_create_issue_button_present(
            self)

    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Create an issue with missing required field")
    def test_create_issue_with_missing_required_field(self):
        Dashboard.start_create_issue(self)
        CreateIssue.create_issue(self, project, issue, "", original_estimate, remaining_estimate)
        CreateIssue.submit_issue(self)
        assert CreateIssue.is_error_message_present(self)
        CreateIssue.cancel_creating_issue(self)

    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Create an issue with parameter length longer that supported")
    def test_create_issue_with_parameter_text_length_longer_than_supported(self):
        Dashboard.start_create_issue(self)
        CreateIssue.create_issue(self, project, issue, long_summary, original_estimate, remaining_estimate)
        CreateIssue.submit_issue(self)
        assert CreateIssue.is_error_message_present(self)


@pytest.mark.usefixtures("driver_init")
class TestSearchIssue:
    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Search previous created issue")
    def test_search_previous_created_issue(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, password)
        Dashboard.click_my_open_issues_menu_item(self)
        MyOpenIssues.get_summary_created_issue(self)
        assert MyOpenIssues.get_summary_created_issue(self) == CreateIssue.summary

    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Search ""No results"" issue")
    def test_search_no_results_issue(self):
        Dashboard.click_search_for_issues_menu_item(self)
        SearchPage.start_search_issue(self, keywords)
        assert keywords in SearchPage.get_summary_searched_issue(self)


@pytest.mark.usefixtures("driver_init")
class TestUpdateIssue:
    @pytest.mark.skip
    @allure.tag('ui')
    @allure.title("Update previous created issue")
    def test_update_previous_created_issue(self):
        LoginPage.open_url(self, base_url)
        LoginPage.login_to_jira(self, username, password)
        Dashboard.click_my_open_issues_menu_item(self)
        MyOpenIssues.get_summary_created_issue(self)
        MyOpenIssues.update_current_summary(self)
        assert "UPDATED" in MyOpenIssues.get_updated_summary(self)
        MyOpenIssues.update_current_priority(self)
        assert "High" in MyOpenIssues.get_updated_priority(self)


class TestsUsingApi:
    @pytest.mark.api
    @allure.tag('api')
    @allure.title("Login using api")
    @pytest.mark.parametrize(
        "http_response, expected",
        [
            # Login OK
            (API.login_by_api(base_url_api, username, password).status_code, 200),

            # Wrong password, AUTHENTICATED FAILED
            (API.login_by_api(base_url_api, username, wrong_credentials).status_code, 401),

            # Wrong username, AUTHENTICATED FAILED
            (API.login_by_api(base_url_api, wrong_credentials, password).status_code, 401)

        ]
    )
    def test_login_to_jira_by_api(self, http_response, expected):
        assert http_response == expected

    @pytest.mark.api
    @allure.tag('api')
    @allure.title("Create issue using api")
    @pytest.mark.parametrize(

        "http_response, expected",
        [
            # with all required fields
            (API.create_issue_by_api(issue, create_issue_endpoint, CreateIssue.created_by_api_summary,
                                     assignee=username,
                                     priority=priority, headers=headers), 201),

            # with missing required fields
            (API.create_issue_by_api(issue, create_issue_endpoint, CreateIssue.created_by_api_summary,
                                     assignee=username,
                                     priority="", headers=headers), 400),

            # with parameter text length, longer than supported
            (API.create_issue_by_api(issue, create_issue_endpoint, long_summary,
                                     assignee=username,
                                     priority=priority, headers=headers), 400)

        ]
    )
    def test_create_issue_in_jira_by_api(self, http_response, expected):
        assert http_response.status_code == expected

    @pytest.mark.api
    @allure.tag('api')
    @allure.title("Search issue using api")
    @pytest.mark.parametrize(

        "http_response, expected",
        [
            # One result
            (API.search_issue_by_api(search_issue_endpoint, summary="Created_by_API", max_results=1, headers=headers),
             200),

            # Five results
            (API.search_issue_by_api(search_issue_endpoint, summary="Created", max_results=5, headers=headers), 200),

            # Non-existed issue
            (API.search_issue_by_api(search_issue_endpoint, summary="", max_results=1, headers=headers), 400)
        ]
    )
    def test_search_issue_in_jira_by_api(self, http_response, expected):
        assert http_response.status_code == expected

    @pytest.mark.api
    @allure.tag('api')
    @allure.title("Update issue using api")
    @pytest.mark.parametrize(
        # create_and_update_issue_by_api(issue, create_endpoint, summary, assignee, priority,
        #                                        new_summary, new_assignee, new_priority, headers):
        "http_response, expected",
        [
            # Updated summary
            (
                    API.create_and_update_issue_by_api(issue, create_issue_endpoint,
                                                       summary=CreateIssue.created_by_api_summary,
                                                       assignee=username, priority=priority, new_summary="Updated",
                                                       new_assignee=username, new_priority=priority, headers=headers),
                    204),

            #  + Updated assignee
            (
                    API.create_and_update_issue_by_api(issue, create_issue_endpoint,
                                                       summary=CreateIssue.created_by_api_summary,
                                                       assignee=username, priority=priority,
                                                       new_summary="Updated",
                                                       new_assignee="webinar5", new_priority=priority,
                                                       headers=headers),
                    204),

            #  + Updated priority
            (
                    API.create_and_update_issue_by_api(issue, create_issue_endpoint,
                                                       summary=CreateIssue.created_by_api_summary,
                                                       assignee=username, priority=priority, new_summary="Updated",
                                                       new_assignee="webinar5", new_priority="Low", headers=headers),
                    204)

        ]
    )
    def test_update_issue_in_jira_by_api(self, http_response, expected):
        assert http_response.status_code == expected
