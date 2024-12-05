import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *
from locators import *

class TestRegistrationPage:

    def test_registration_succesfull(self,chrome_driver): #я не понял, в какой момент нужно тестировать пустое поле, в момент регистрации или же после регистрации. Оставил вариант после регистрации, потому что ошибка идентична тесту домена в поле email (следующий тест в классе)
        driver = chrome_driver
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME).send_keys(UserValue.USER_NAME)
        email = UserValue.REGISTRATION_GENERATED_EMAIL
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(UserValue.USER_PASSWORD)
        driver.find_element(*REGISTRATION_ACCEPT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*EMAIL_INPUT).click()
        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).click()
        driver.find_element(*PASSWORD_INPUT).send_keys(UserValue.USER_PASSWORD)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCEPT_LOGIN_BUTTON))
        driver.find_element(*ACCEPT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ORDER_BUTTON))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(REGISTRATION_NAME))
        length_value = driver.find_element(*REGISTRATION_NAME).get_dom_attribute('disabled value')
        assert length_value != 0

    def test_email_field_contains_domen(self,chrome_driver):
        driver = chrome_driver
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME).send_keys(UserValue.USER_NAME)
        driver.find_element(*REGISTRATION_EMAIL).send_keys(UserValue.UNCORRECT_EMAIL)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(UserValue.USER_PASSWORD)
        driver.find_element(*REGISTRATION_ACCEPT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MESSAGE_USER_ALREADY_EXISTS))
        login_error_message = driver.find_element(*MESSAGE_USER_ALREADY_EXISTS).text
        assert login_error_message == Messages.REGISTRATION_LOGIN_ERROR_MESSAGE

    def test_uncorrect_len_password(self,chrome_driver):
        driver = chrome_driver
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME).send_keys(UserValue.USER_NAME)
        driver.find_element(*REGISTRATION_EMAIL).send_keys(UserValue.REGISTRATION_GENERATED_EMAIL)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(UserValue.UNCORRECT_LEN_PASSWORD_REGISTRATION)
        driver.find_element(*REGISTRATION_ACCEPT_BUTTON).click()
        assert driver.find_element(*REGISTRATION_UNCORRECT_PASSWORD).text == Messages.REGISTRATION_UNCORRECT_PASSWORD_MESSAGE
