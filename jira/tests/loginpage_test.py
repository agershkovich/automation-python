from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from jira.pages.loginpage import LoginPage

creds = "OlegAverkin"
fake_creds = "fake_user"
base_url = "https://jira.hillel.it"
auth_url = base_url + "/secure/RapidBoard.jspa?projectKey=WEBINAR"
login_title = "Log in - Hillel IT School JIRA"


class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    def test_check_title(self):
        self.login_page.open(auth_url)
        assert self.login_page.get_title() == login_title

    def test_login_with_wrong_username(self):
        self.login_page.open(auth_url)
        self.login_page.login_to_jira(creds, fake_creds)
        assert self.login_page.get_title() == login_title
