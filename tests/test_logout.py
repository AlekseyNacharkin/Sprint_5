import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *
from locators import *

class TestLogout:
    def test_logout_from_personal_account(self,open_personal_account):
        driver = open_personal_account
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGOUT_BUTTON_FROM_PERSONAL_ACCOUNT))
        driver.find_element(*LOGOUT_BUTTON_FROM_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCEPT_LOGIN_BUTTON))
        assert driver.current_url == URLs.LOGIN_URL
