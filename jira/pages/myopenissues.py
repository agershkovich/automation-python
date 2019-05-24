from selenium.webdriver.common.by import By

from jira.pages.basepage import BasePage
from jira.utils.waiters_and_actions import UIInteractions


class MyOpenIssues(BasePage):
    # xpath = "//*[@class='issue-link-summary'][contains(text()," + " '" + CreateIssue.summary + "'" + ")]"
    # created_issue_summary = (By.XPATH, xpath)
    my_open_issues_summary_value = (By.ID, "summary-val")

    def get_summary_created_issue(self):
        return UIInteractions.get_text(self.driver, MyOpenIssues.my_open_issues_summary_value)

    def get_created_issue_url(self):
        return BasePage.current_url(self).split("?")[0]
