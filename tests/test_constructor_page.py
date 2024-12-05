from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import *
from locators import *

class TestConstructorPage:
    def test_bun_section_opening(self,authorization):
        driver = authorization
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUN_SECTION))
        assert SubclassForTestConstructor.SELECTED_SECTION_OF_CONSTRUCTOR in driver.find_element(*BUN_SECTION).get_dom_attribute('class')

    def test_sauce_section_opening(self,authorization):
        driver = authorization
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SAUCE_SECTION))
        driver.find_element(*SAUCE_SECTION).click()
        assert SubclassForTestConstructor.SELECTED_SECTION_OF_CONSTRUCTOR in driver.find_element(*SAUCE_SECTION).get_dom_attribute('class')

    def test_fillings_section_opening(self,authorization):
        driver = authorization
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(FILLINGS_SECTION))
        driver.find_element(*FILLINGS_SECTION).click()
        assert SubclassForTestConstructor.SELECTED_SECTION_OF_CONSTRUCTOR in driver.find_element(*FILLINGS_SECTION).get_dom_attribute('class')
