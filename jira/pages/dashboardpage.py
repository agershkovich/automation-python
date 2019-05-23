from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from jira.pages.basepage import BasePage
from jira.utils.waiters_and_actions import UIInteractions


class Dashboard(BasePage):
    avatar_icon = (By.CLASS_NAME, "aui-avatar-inner")
    create_button_id = (By.ID, "create_link")

    def is_dashboard_avatar_icon_present(self):
        try:
            UIInteractions.waiting_for_element_visibility(self.driver, Dashboard.avatar_icon)
        except NoSuchElementException:
            return False
        return True

    def start_create_issue(self):
        UIInteractions.waiting_for_element_visibility(self.driver, Dashboard.create_button_id)
        UIInteractions.click(self.driver, Dashboard.create_button_id)