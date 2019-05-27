from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from jira.pages.basepage import BasePage
from jira.utils.waiters_and_actions import UIInteractions


class MyOpenIssues(BasePage):
    # xpath = "//*[@class='issue-link-summary'][contains(text()," + " '" + CreateIssue.summary + "'" + ")]"
    # created_issue_summary = (By.XPATH, xpath)
    my_open_issues_summary_value = (By.ID, "summary-val")
    my_open_issues_editable_summary_value = (By.ID, "summary")
    my_open_issues_priority_value = (By.ID, "priority-val")
    my_open_issues_priority_editable_value = (By.ID, "priority-field")

    def get_summary_created_issue(self):
        return str(UIInteractions.get_text(self.driver, MyOpenIssues.my_open_issues_summary_value))

    def get_created_issue_url(self):
        return BasePage.current_url(self).split("?")[0]

    def update_current_summary(self):
        UIInteractions.click(self.driver, MyOpenIssues.my_open_issues_summary_value)
        sleep(2)
        UIInteractions.input_issue_value(self.driver, MyOpenIssues.my_open_issues_editable_summary_value, " UPDATED")

    def get_updated_summary(self):
        sleep(2)
        self.driver.refresh()
        return UIInteractions.get_text(self.driver, MyOpenIssues.my_open_issues_summary_value)

    def update_current_priority(self):
        UIInteractions.click(self.driver, MyOpenIssues.my_open_issues_priority_value)
        sleep(2)
        UIInteractions.waiting_for_element_visibility(self.driver,
                                                      MyOpenIssues.my_open_issues_priority_editable_value).send_keys(
            Keys.BACKSPACE)
        sleep(2)
        UIInteractions.waiting_for_element_visibility(self.driver,
                                                      MyOpenIssues.my_open_issues_priority_editable_value).send_keys(
            "High")
        sleep(2)
        UIInteractions.waiting_for_element_visibility(self.driver,
                                                      MyOpenIssues.my_open_issues_priority_editable_value).send_keys(
            Keys.ENTER)
        UIInteractions.waiting_for_element_visibility(self.driver,
                                                      MyOpenIssues.my_open_issues_priority_editable_value).send_keys(
            Keys.ENTER)

    def get_updated_priority(self):
        sleep(2)
        return UIInteractions.get_text(self.driver, MyOpenIssues.my_open_issues_priority_value)
