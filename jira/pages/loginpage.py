from jira.pages.basepage import BasePage
from jira.utils.waiters_and_actions import UIInteractions

# login_error = "aui-message aui-message-error"
create_issue_id = "create_link"


class LoginPage(BasePage):
    login_form_id = 'login-form-username'
    password_form_id = 'login-form-password'
    login_button_id = 'login'

    def input_username(self, username):
        UIInteractions.input_text_value(self.driver, LoginPage.login_form_id, username)

    def input_password(self, password):
        UIInteractions.input_text_value(self.driver, LoginPage.password_form_id, password)

    def submit_credentials(self):
        UIInteractions.submit(self.driver, LoginPage.login_button_id)
