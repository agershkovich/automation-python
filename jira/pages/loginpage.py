from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from jira.pages.basepage import BasePage
from jira.utils.waiters_and_actions import UIInteractions


class LoginPage(BasePage):
    login_form_id = (By.ID, "login-form-username")
    password_form_id = (By.ID, "login-form-password")
    login_button_id = (By.ID, 'login')
    error_message = (By.CLASS_NAME, "aui-message-error")
    avatar_icon = (By.CLASS_NAME, "aui-avatar-inner")

    def input_username(self, username):
        UIInteractions.input_text_value(self.driver, LoginPage.login_form_id, username)

    def input_password(self, password):
        UIInteractions.input_text_value(self.driver, LoginPage.password_form_id, password)

    def submit_credentials(self):
        UIInteractions.submit(self.driver, LoginPage.login_button_id)

    def is_error_message_present(self):
        try:
            UIInteractions.waiting_for_element_visibility(self.driver, LoginPage.error_message)
        except NoSuchElementException:
            return False
        return True
