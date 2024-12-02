from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import *
from locators import *

class TestPersonalAccount:
    def test_personal_account(self,open_personal_account):
        driver = open_personal_account
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EDIT_PROFILE_BUTTON))
        driver.find_element(*EDIT_PROFILE_BUTTON).click()
        assert driver.current_url == PERSONAL_ACCOUNT_URL
