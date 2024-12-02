from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *
from locators import *

class TestRegistrationPage:
    def test_registration_uncorrect_len_password(self,chrome_driver):
        driver = chrome_driver
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME).send_keys(USER_NAME)
        driver.find_element(*REGISTRATION_EMAIL).send_keys(USER_EMAIL)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(UNCORRECT_LEN_PASSWORD_REGISTRATION)
        driver.find_element(*REGISTRATION_ACCEPT_BUTTON).click()
        assert driver.find_element(*REGISTRATION_UNCORRECT_PASSWORD).text == REGISTRATION_UNCORRECT_PASSWORD_MESSAGE

    def test_registration_name_len(self,open_personal_account):
        driver = open_personal_account
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(REGISTRATION_NAME))
        length_value = driver.find_element(*REGISTRATION_NAME).get_dom_attribute('disabled value')
        assert length_value != 0

    def test_email_field_contains_login_and_domen(self,open_personal_account):
        driver = open_personal_account
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_FIELD_EMAIL_VALUE))
        email_value = driver.find_element(*LOGIN_FIELD_EMAIL_VALUE).get_dom_attribute('value')
        assert '@gmail.com' in email_value





