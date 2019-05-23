from time import sleep

import pytest

from jira.pages.loginpage import LoginPage

base_url = "https://jira.hillel.it/secure/Dashboard.jspa"
title = "System Dashboard - Hillel IT School JIRA"
username = "AlexeyGershkovich"
password = "AlexeyGershkovich"
wrong_creds = "Dummy"


@pytest.mark.usefixtures("driver_init")
class TestLoginPage:


    def test_open_jira_url(self):
        LoginPage.open_url(self, base_url)
        assert self.driver.title == title

        sleep(3)

    def test_correct_username_but_wrong_password(self):
        LoginPage.open_url(self, base_url)
        LoginPage.input_username(self, username)
        LoginPage.input_password(self, password)
        LoginPage.submit_credentials(self)

        sleep(3)
