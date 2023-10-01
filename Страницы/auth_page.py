from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url if url else "https://b2c.passport.rt.ru"
        # super().__init__(driver, timeout) - обращаемся к методу __init__ нашего
        # родительского класса BasePage, так как наш новый метод __init__ затрёт его
        super().__init__(web_driver, url)
        # создаем нужные элементы

    phone = WebElement(id='username')

    email = WebElement(id='username')

    login = WebElement(id='username')

    personal_account = WebElement(id='username')

    password = WebElement(id='password')

    btn = WebElement(id='kc-login')   # войти

    recovery = WebElement(id='forgot_password')  # забыл пароль

    registration = WebElement(id='kc-register')

    auth_code = WebElement(css_selector='input[id="address"]')

    get_code = WebElement(id='otp_get_code')

    link_phone = WebElement(class_name='rt-radio__circle')

    link_email = WebElement(link_text='По e-mail')

    go_click = WebElement(css_selector='button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded reset-choice-form__reset-btn"]')

    rt_code = WebElement(id='rt-code-0')

    captcha = WebElement(alt='Captcha')  # Капча

    symbol = WebElement(id='captcha')  # окно капчи

    contin = WebElement(id='reset')  # Кнопка "Продолжить"

    new_pass = WebElement(id='password-new')  # новый пароль при восстановлении

    confirm = WebElement(id='password-confirm')   #  подтверждение нового пароля

    save = WebElement(id='t-btn-reset-pass')  # кнопка "Сохранить"

    name = WebElement(name='firstName')

    lastname = WebElement(name='lastName')

    region = WebElement(css_selector="#page-right > div > div > div > form > div:nth-of-type(2) > div > div > input")

    arrow = WebElement(css_selector='#page-right > div > div > div > form > div.rt-select.rt-select--search.register-form__dropdown > div > div > span.rt-input__mask > <span."rt-input__mask-start">Новосибирская обл</span>')

    email_or_phone = WebElement(id='address')

    confirmation = WebElement(id='password-confirm')

    register = WebElement(name='register')  # зарегистрироваться