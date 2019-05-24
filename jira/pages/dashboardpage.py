from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from jira.pages.basepage import BasePage
from jira.pages.createissue import CreateIssue
from jira.pages.myopenissues import MyOpenIssues
from jira.pages.searchpage import SearchPage
from jira.utils.waiters_and_actions import UIInteractions


class Dashboard(BasePage):
    avatar_icon = (By.CLASS_NAME, "aui-avatar-inner")
    create_button = (By.ID, "create_link")
    issues_button = (By.ID, "find_link")
    my_open_issues_menu_item = (By.ID, "filter_lnk_my_lnk")
    search_for_issues_menu_item = (By.ID, "issues_new_search_link_lnk")

    def is_dashboard_avatar_icon_present(self):
        try:
            UIInteractions.waiting_for_element_visibility(self.driver, Dashboard.avatar_icon)
        except NoSuchElementException:
            return False
        return True

    def is_dashboard_create_issue_button_present(self):
        try:
            UIInteractions.waiting_for_element_visibility(self.driver, Dashboard.create_button)
        except NoSuchElementException:
            return False
        return True

    def start_create_issue(self):
        sleep(3)
        UIInteractions.click(self.driver, Dashboard.create_button)
        return CreateIssue(self.driver)

    def click_my_open_issues_menu_item(self):
        UIInteractions.click(self.driver, Dashboard.issues_button)
        UIInteractions.click(self.driver, Dashboard.my_open_issues_menu_item)
        return MyOpenIssues(self.driver)

    def click_search_for_issues_menu_item(self):
        UIInteractions.click(self.driver, Dashboard.issues_button)
        UIInteractions.click(self.driver, Dashboard.search_for_issues_menu_item)
        return SearchPage(self.driver)
