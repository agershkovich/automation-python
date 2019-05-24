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
    def input_issue_value(driver, locator, value):
        UIInteractions.waiting_for_element_is_clickable(driver, locator).click()
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(Keys.DELETE)
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(value)
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(Keys.ENTER)

    @staticmethod
    def submit(driver, locator):
        UIInteractions.waiting_for_element_visibility(driver, locator).submit()

    @staticmethod
    def get_text(driver, locator):
        return UIInteractions.waiting_for_element_visibility(driver, locator).text

    @staticmethod
    def sing_sen_maker():
        s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie",
                   "This cool guy my gardener met yesterday", "Superman"]
        p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys",
                   "All of a cattery's cats",
                   "The multitude of sloths living under your bed", "Your homies",
                   "Like, these, like, all these people",
                   "Supermen"]
        s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on",
                   "retards", "meows on", "flees from", "tries to automate", "explodes"]
        p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard",
                   "meow on", "flee from", "try to automate", "explode"]
        infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.",
                       "to be able to make toast explode.", "to know more about archeology."]

        import random

        return (random.choice(s_nouns) + " " + random.choice(s_verbs) + " " + random.choice(
            s_nouns).lower() or random.choice(
            p_nouns).lower() + " " + random.choice(p_verbs) + " " + random.choice(infinitives))
