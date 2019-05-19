import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_for_element(self, element, selector_type: By):
        self.wait.until(EC.presence_of_element_located((selector_type, element)))
        self.wait.until(EC.visibility_of_element_located((selector_type, element)))
        self.wait.until(EC.element_to_be_clickable((selector_type, element)))

    def click_on_element(self, element, selector_type: By):
        self.wait.until(EC.presence_of_element_located((selector_type, element)))
        self.wait.until(EC.visibility_of_element_located((selector_type, element)))
        self.wait.until(EC.element_to_be_clickable((selector_type, element)))
        el = self.driver.find_element(selector_type, element)
        el.click()

    #
    def browser_refresh(self):
        self.driver.refresh()

    #
    def type_to_elem(self, element, selector_type: By, text, clean=True, click_enter=False, type_delay=False):
        self.wait.until(EC.presence_of_element_located((selector_type, element)))
        self.wait.until(EC.visibility_of_element_located((selector_type, element)))
        self.wait.until(EC.element_to_be_clickable((selector_type, element)))
        elem = self.driver.find_element(selector_type, element)
        elem.click()
        if clean:
            elem.clear()
        if type_delay:
            for i in text:
                elem.send_keys(i)
                time.sleep(0.1)
        elem.send_keys(text)
        if click_enter:
            elem.send_keys(Keys.ENTER)
