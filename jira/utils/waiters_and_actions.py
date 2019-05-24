from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class UIInteractions:
    timeout = 10

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
        UIInteractions.waiting_for_element_is_clickable(driver, locator).click()

    @staticmethod
    def input_text_value(driver, locator, value):
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(value)

    @staticmethod
    def input_create_issue_value(driver, locator, value):
        UIInteractions.waiting_for_element_is_clickable(driver, locator).click()
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(Keys.DELETE)
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(value)
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(Keys.ENTER)

    @staticmethod
    def submit(driver, locator):
        UIInteractions.waiting_for_element_visibility(driver, locator).submit()
