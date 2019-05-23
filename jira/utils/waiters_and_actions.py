from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class UIInteractions:
    timeout = 15
    @staticmethod
    def waiting_for_element_visibility(driver, locator):
        return WebDriverWait(driver, UIInteractions.timeout).until(
            ec.visibility_of_element_located(locator))

    @staticmethod
    def waiting_for_element_is_clickable(driver, locator):
        return WebDriverWait(driver, UIInteractions.timeout).until(
            ec.element_to_be_clickable(locator))

    @staticmethod
    def click(driver, locator):
        elem = UIInteractions.waiting_for_element_is_clickable(driver, locator)
        elem.click()

    @staticmethod
    def input_text_value(driver, locator, value):
        elem = UIInteractions.waiting_for_element_visibility(driver, locator)
        elem.clear()
        elem.send_keys(value)

    @staticmethod
    def submit(driver, locator):
        elem = UIInteractions.waiting_for_element_visibility(driver, locator)
        elem.submit()