from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    def __init__(self, driver):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(driver)


