from selenium.webdriver.common.by import By

from jira.pages.basepage import BasePage
from jira.utils.waiters_and_actions import UIInteractions


class SearchPage(BasePage):
    issue_search_query_value = (By.ID, "searcher-query")
    issue_summary_value = (By.ID, "summary-val")

    def start_search_issue(self, keywords):
        UIInteractions.input_issue_value(self.driver, SearchPage.issue_search_query_value, keywords)

    def get_summary_searched_issue(self):
        self.driver.refresh()
        print(UIInteractions.get_text(self.driver, SearchPage.issue_summary_value))
        return UIInteractions.get_text(self.driver, SearchPage.issue_summary_value)
