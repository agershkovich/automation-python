from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
