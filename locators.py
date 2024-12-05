from selenium.webdriver.common.by import By


EMAIL_INPUT = (By.XPATH, "//input[@name='name']") # Поле для ввода Email при авторизации
PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") # Поле для ввода пароля при авторизации
ACCEPT_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка "Войти" для подтверждения входа в аккаунт
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") # кнопка "Войти в аккаунт" для перехода в окно входа в аккаунт
ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # кнопка "Оформить заказ"
PERSONAL_ACCOUNT = (By.XPATH, ".//a[@class = 'AppHeader_header__link__3D_hX']//p[contains(text(),'Личный Кабинет')]") # Кнопка личный кабинет
REGISTRATION_BUTTON = (By.XPATH, ".//p[@class='undefined text text_type_main-default text_color_inactive mb-4']//a[@class='Auth_link__1fOlj']") # Кнопка "Зарегистрироваться" в окне авторизации
REGISTRATION_NAME = (By.XPATH, ".//label[contains(text(),'Имя')]/following-sibling::input") # Поле имя для регистрации пользователя
REGISTRATION_EMAIL = (By.XPATH, ".//label[contains(text(),'Email')]/following-sibling::input") # Поле почта для регистрации пользователя
REGISTRATION_PASSWORD = (By.XPATH, ".//label[contains(text(),'Пароль')]/following-sibling::input") # Поле пароль для регистрации пользователя
REGISTRATION_ACCEPT_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # Кнопка подтверждения регистрации пользователя
REGISTRATION_UNCORRECT_PASSWORD = (By.XPATH, ".//p[@class='input__error text_type_main-default']") #Окно с ошибкой о неверном пароле
REGISTRAION_BUTTON_IN_PERSONAL_ACCOUNT = (By.XPATH, './/a[@class="Auth_link__1fOlj" and @href="/register"]') # Кнопка перехода в окно регистрации из личного аккаунта
LOGIN_BUTTON_IN_REGISTRATION_WINDOW = (By.XPATH, './/a[@class="Auth_link__1fOlj" and @href="/login"]') # Кнопка "Войти в аккаунт" из окна регистрации пользователя
REGENARATE_PASSWORD_IN_REGISTRATION_WINDOW = (By.XPATH, './/a[@class="Auth_link__1fOlj" and @href="/forgot-password"]') # Кнопка "Забыли пароль"
EDIT_PROFILE_BUTTON = (By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']") # Кнопка "Изменить профиль"
LOGO_STELLAR_BURGERS_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # Кнопка логотипа STELLAR_BURGERS
CONSTRUCTOR_STELLAR_BURGERS_BUTTON = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(),'Конструктор')]") # Кнопка конструктора бургеров
LOGOUT_BUTTON_FROM_PERSONAL_ACCOUNT = (By.XPATH, ".//button[contains(text(),'Выход')]") # Кнопка "Выйти" в личном кабинете
BUN_SECTION = (By.XPATH,".//span[contains(text(),'Булки')]/parent::div") # Кнопка "Булки" в конструкторе бургера
SAUCE_SECTION = (By.XPATH, ".//span[contains(text(),'Соусы')]/parent::div") # Кнопка "Соусы" в конструкторе бургера
FILLINGS_SECTION = (By.XPATH, ".//span[contains(text(),'Начинки')]/parent::div") # Кнопка "Начинки" в конструкторе бургера
LOGIN_FIELD_EMAIL_VALUE = (By.XPATH, ".//label[contains(text(),'Логин')]/following-sibling::input") # Кнопка для проверки логина (email)
MESSAGE_USER_ALREADY_EXISTS = (By.XPATH, ".//p[@class='input__error text_type_main-default']")