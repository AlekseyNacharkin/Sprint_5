from locators import *

class TestOpeningConstrictor:
    def test_opening_constructor_click_on_logo(self,open_personal_account):
        driver = open_personal_account
        current_url = driver.current_url
        driver.find_element(*LOGO_STELLAR_BURGERS_BUTTON).click()
        assert current_url != driver.current_url

    def test_opening_constructor_click_on_constructor_button(self,open_personal_account):
        driver = open_personal_account
        current_url = driver.current_url
        driver.find_element(*CONSTRUCTOR_STELLAR_BURGERS_BUTTON).click()
        assert current_url != driver.current_url
