import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import *
from locators import *


@pytest.fixture()
def mozila_driver():
    driver = webdriver.Firefox()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def authorization(chrome_driver):
    driver = chrome_driver
    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys(UserValue.USER_EMAIL)
    driver.find_element(*PASSWORD_INPUT).send_keys(UserValue.USER_PASSWORD)
    driver.find_element(*ACCEPT_LOGIN_BUTTON).click()
    return driver

@pytest.fixture()
def open_personal_account(authorization):
    driver = authorization
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT))
    driver.find_element(*PERSONAL_ACCOUNT).click()
    return driver

