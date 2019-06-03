from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from jira.pages.basepage import BasePage
from jira.utils.waiters_and_actions import UIInteractions


class CreateIssue(BasePage):
    jira_dialog_heading = (By.CLASS_NAME, "jira-dialog-heading")
    project_dropdown_field = (By.ID, "project-field")
    issuetype_dropdown_field = (By.ID, "issuetype-field")
    summary_input_field = (By.ID, "summary")
    text_switch_button = (By.PARTIAL_LINK_TEXT, "Text")
    description_input_field = (By.ID, "description")
    create_issue_submit_button = (By.ID, "create-issue-submit")
    priority_dropdown_field = (By.ID, "priority-field")
    labels_input_field = (By.ID, "labels-textarea")
    linked_issues_dropdown_list = (By.ID, "issuelinks-linktype")
    issue_input_field = (By.ID, "issuelinks-issues-textarea")
    original_estimate_input_field = (By.ID, "timetracking_originalestimate")
    remaining_estimate_input_field = (By.ID, "timetracking_remainingestimate")
    assignee_link = (By.ID, "assign-to-me-trigger")
    epic_link_input_field = (By.ID, "customfield_10000-field")
    security_token_missing = (By.ID, "atl_token_retry_button")
    error_message = (By.CLASS_NAME, "error")
    cancel_button = (By.CSS_SELECTOR, "a.cancel")

    random_summary = UIInteractions.sing_sen_maker()
    summary = random_summary
    created_by_api_summary = "Created_by_API - " + random_summary

    def is_create_issue_page_present(self):
        try:
            UIInteractions.waiting_for_element_visibility(self.driver, CreateIssue.jira_dialog_heading)
        except NoSuchElementException:
            return False
        return True

    def is_security_token_missing(self):
        try:
            UIInteractions.waiting_for_element_visibility(self.driver, CreateIssue.security_token_missing)
        except None:
            return False
        return True

    def is_error_message_present(self):
        try:
            UIInteractions.waiting_for_element_visibility(self.driver, CreateIssue.error_message)
        except None:
            return False
        return True

    def create_issue(self, project, issue, summary, original_estimate, remaining_estimate):
        UIInteractions.click(self.driver, CreateIssue.assignee_link)
        UIInteractions.input_text_value(self.driver, CreateIssue.summary_input_field, "")
        UIInteractions.input_text_value(self.driver, CreateIssue.summary_input_field, summary)
        UIInteractions.input_text_value(self.driver, CreateIssue.original_estimate_input_field, original_estimate)
        UIInteractions.input_text_value(self.driver, CreateIssue.remaining_estimate_input_field, remaining_estimate)
        UIInteractions.input_issue_value(self.driver, CreateIssue.project_dropdown_field, project)
        UIInteractions.input_issue_value(self.driver, CreateIssue.issuetype_dropdown_field, issue)

    def submit_issue(self):

        UIInteractions.submit(self.driver, CreateIssue.create_issue_submit_button)

        if CreateIssue.is_security_token_missing(self):
            UIInteractions.click(self.driver, CreateIssue.security_token_missing)
            UIInteractions.submit(self.driver, CreateIssue.create_issue_submit_button)

        sleep(3)

    def cancel_creating_issue(self):

        UIInteractions.click(self.driver, CreateIssue.cancel_button)

        alert = self.driver.switch_to.alert

        if alert:
            alert.accept()
