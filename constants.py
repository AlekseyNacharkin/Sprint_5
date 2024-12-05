import random

class URLs:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"
    PERSONAL_ACCOUNT_URL = "https://stellarburgers.nomoreparties.site/account/profile"

class UserValue:
    USER_EMAIL = "nacharkin_9916@gmail.com"
    USER_PASSWORD = "123456"
    USER_NAME = "Алексей"
    UNCORRECT_EMAIL = "nacharkin_9916"
    UNCORRECT_LEN_PASSWORD_REGISTRATION = "12345"
    REGISTRATION_GENERATED_EMAIL = f"nacharkin{random.randint(100, 999)}@gmail.com"

class Messages:
    REGISTRATION_UNCORRECT_PASSWORD_MESSAGE = "Некорректный пароль"
    REGISTRATION_LOGIN_ERROR_MESSAGE = "Такой пользователь уже существует"

class SubclassForTestConstructor:
    SELECTED_SECTION_OF_CONSTRUCTOR = "tab_tab_type_current__2BEPc"


