from selenium.webdriver.support.wait import WebDriverWait
from constants import *
from locators import *
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage:
    def test_authorization_with_login_button(self,authorization):
        driver = authorization
        order_button_in_dom = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert order_button_in_dom.is_displayed()

    def test_authorization_with_personal_account(self,chrome_driver):
        driver = chrome_driver
        driver.get(BASE_URL)
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*ACCEPT_LOGIN_BUTTON).click()
        order_button_in_dom = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert order_button_in_dom.is_displayed()

    def test_authorization_from_registration_window(self,chrome_driver):
        driver = chrome_driver
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*REGISTRAION_BUTTON_IN_PERSONAL_ACCOUNT).click() #нажми кнопку зарегистрироваться
        driver.find_element(*LOGIN_BUTTON_IN_REGISTRATION_WINDOW).click()
        driver.find_element(*EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*ACCEPT_LOGIN_BUTTON).click()
        order_button_in_dom = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert order_button_in_dom.is_displayed()

    def test_authorization_from_regenerate_password_field(self,chrome_driver):
        driver = chrome_driver
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*REGENARATE_PASSWORD_IN_REGISTRATION_WINDOW).click()
        driver.find_element(*LOGIN_BUTTON_IN_REGISTRATION_WINDOW).click()
        driver.find_element(*EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*ACCEPT_LOGIN_BUTTON).click()
        order_button_in_dom = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert order_button_in_dom.is_displayed()



