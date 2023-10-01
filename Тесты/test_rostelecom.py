import pytest
import random
import time

from pages.auth_page import AuthPage
from settings import valid_email, valid_password, valid_login, valid_phone, valid_pers_acc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By


# TC_SAV-005 - номер теста в тест-кейсах.
@pytest.mark.positive
def test_authorisation_phone(web_browser):

    page = AuthPage(web_browser)

    page.phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    page._web_driver.save_screenshot('screenshots/test_authorisation_phone.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url(), 'Incorrect authorization'


# TC_SAV-005 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
@pytest.mark.xfail(reason="assert по тексту 'Неверный логин или пароль'")
def test_authorisation_phone_negative(web_browser):

    page = AuthPage(web_browser)

    page.phone.send_keys('+796078463565')   # invalid phone

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    # # Устанавливаем явное ожидание
    # WDW(web_browser, 5).until(EC.presence_of_element_located((By.XPATH, '//[@id="page-right"]')))

    # # Сохраняем в переменную message_err элементы с данными
    # message_err = web_browser.find_elements(By.ID, 'page-right')
    # for i in range(len(message_err)):
    #     data_mess = message_err[i].text.replace('\n', '').replace(',', "").replace("'", "")
    #     split_data_mess = data_mess.split(' ')
    #     print(split_data_mess)

    page._web_driver.save_screenshot('screenshots/test_authorisation_phone_negative.png')

    # assert split_data_mess == ["'Неверный', 'логин', 'или', 'пароль'"], "No caption"
    # assert 'Неверный логин или пароль' in ' '.join(split_data_mess), "No caption"

    # assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in page.get_current_u

    # Поле "Мобильный телефон" в номере '+7960784635465' отсекает все цифры после двенадцатой, поэтому происходит авторизация
    # При вводе латиницы в номере '+7960784635465a' происходит переход на кнопку "Логин"
    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url()


# TC_SAV-006 - номер теста в тест-кейсах.
@pytest.mark.positive
def test_authorisation_email(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys(valid_email)

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    page._web_driver.save_screenshot('screenshots/test_authorisation_email.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url()


# TC_SAV-006 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
def test_authorisation_email_negative(web_browser):

    page = AuthPage(web_browser)

    # 256 символов
    page.email.send_keys('9ayL2nRwT5dFfXbjK2s5IJDwJjbUk87CWEQ380T4QEgHkrkzpvkftnzohmH6wrFLz4YaKE8bsk6K0Se90oyt7NB7nodhZPW96hCxF2OmsLNtrwR0sairW49gRWJqg1WrFYSrbKOJVBrLtOhlDvY4IxMTVti5aWLt2p6baQPRmLMwormlZ2c46igmxqWnNofYpWE6OalN7BPK1v0B2jSbUARcOIxOWOeMCuYmqOYRKr7MhrHYIHMyiONDiOmUfqXc@mail.ru')

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    page._web_driver.save_screenshot('screenshots/test_authorisation_email_negative.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in page.get_current_url()


# TC_SAV-007 - номер теста в тест-кейсах.
@pytest.mark.positive
def test_authorisation_login(web_browser):

    page = AuthPage(web_browser)

    page.login.send_keys(valid_login)

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    page._web_driver.save_screenshot('screenshots/test_authorisation_login.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url(), 'Incorrect authorization'


# TC_SAV-007 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
def test_authorisation_login_negative(web_browser):

    page = AuthPage(web_browser)

    page.login.send_keys('valid_login13@mail.ru')   # invalid login

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    page._web_driver.save_screenshot('screenshots/test_authorisation_login_negative.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in page.get_current_url()


# TC_SAV-008 - номер теста в тест-кейсах.
@pytest.mark.positive
def test_authorisation_pers_acc(web_browser):

    page = AuthPage(web_browser)

    page.pa.send_keys(valid_pers_acc)

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    page._web_driver.save_screenshot('screenshots/test_authorisation_pers_acc.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url()


# TC_SAV-008 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
def test_authorisation_pers_acc_negative(web_browser):

    page = AuthPage(web_browser)

    # 12 цифр + латиница
    # page.personal_account.send_keys('123456789112a')

    # 1001 цифра
    page.personal_account.send_keys('76884439226025616424603398010574353258795150179353803710823662595228625634742160285564021479495561905510457896574361838119542648657177592951782781440500086142089924581817907267734861878905545859201021281462972353759032981533012108865109740531103229508507157596476061451055494245358330305717747946521466388787748925047411542986427613229772104890774790835632019570814835734555056849723215218897111425690557848762558175913122179682144858379133908184510232492831779762299113788643488934128041039472490467241481986571560407878321853680884503907151023381440298501940726572254483847723092928104283948451461689896115108355542080751331092672645392453720085690083527417424557239640496183844703329772383469913572534178766503716608425628845450752656435550818252837815974107675354815701780115988584782525567230545460893445749276124890282506999915240264722504519933589329025631008185355485856369282705942137783713949563191445696021360289559476979567241647305501320644372192704383371235773766845337191088480083779288')

    page.password.send_keys(valid_password)

    page.btn.click()

    time.sleep(5)  # задержка для учебных целей

    page._web_driver.save_screenshot('screenshots/test_authorisation_pers_acc_negative.png')

    # При вводе латиницы происходит переход на кнопку "Логин"
    # При вводе цифр (в т.ч. 1001 цифру)происходит переход на кнопку "Номер"
    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in page.get_current_url()


# TC_SAV-009 - номер теста в тест-кейсах.
@pytest.mark.positive
@pytest.mark.xfail(reason="ввод email, при переходе на новую страницу")
def test_authorisation_code_email(web_browser):

    page = AuthPage(web_browser)

    page_2 = page.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/'
                      'auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri='
                      'https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.'
                      'rt.ru%252F&state=%7B%22uuid%22%3A%22132CAE44-D901-41BB-A8AC-79C4554A6BEE%22%7D')

    time.sleep(10)

    page_2.auth_code.send_keys(valid_email)

    symbols = page.captcha.get_text()  # текст капчи

    page_2.symbol.send_keys(symbols)  # окно капчи

    time.sleep(5)  # задержка для учебных целей

    page_2.get_code.click()

    page_3 = web_browser.get('https://e.mail.ru/inbox/?back=1')

    element = WDW(web_browser, 15).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span'), 'Ваш код'
    )

    page_3.element.click()

    time.sleep(5)  # задержка для учебных целей

    element_2 = web_browser.find_element(By.TAG_NAME, 'div > p')

    for i in element_2:
        one_elem = i.text.split(' ')
        all_elem = one_elem[2]
        my_code = all_elem.get_text()
        print(my_code)

    page_2.rt_code.send_keys(my_code)

    page_2._web_driver.save_screenshot('screenshots/test_authorisation_code_email.png')

    assert 'https://start.rt.ru/?tab=main' in page_2.get_current_url()


# TC_SAV-010 - номер теста в тест-кейсах.
@pytest.mark.positive
def test_authorisation_code_phone(web_browser):

    page = AuthPage(web_browser)

    page_2 = page.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/'
                      'auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri='
                      'https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.'
                      'rt.ru%252F&state=%7B%22uuid%22%3A%22132CAE44-D901-41BB-A8AC-79C4554A6BEE%22%7D')

    time.sleep(10)

    page_2.auth_code.send_keys(valid_phone)

    page_2.get_code.click()

    page_2.rt_code.send_keys()

    time.sleep(5)  # задержка для учебных целей

    page_2._web_driver.save_screenshot('screenshots/test_authorisation_code_phone.png')

    assert 'https://start.rt.ru/?tab=main' in page_2.get_current_url()


# TC_SAV-010 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
def test_authorisation_code_phone_negative(web_browser):

    page = AuthPage(web_browser)

    page_2 = page.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/'
                      'auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri='
                      'https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.'
                      'rt.ru%252F&state=%7B%22uuid%22%3A%22132CAE44-D901-41BB-A8AC-79C4554A6BEE%22%7D')

    time.sleep(10)

    page_2.auth_code.send_keys(valid_phone)

    page_2.get_code.click()

    page_2.rt_code.send_keys()

    time.sleep(5)  # задержка для учебных целей

    page_2._web_driver.save_screenshot('screenshots/test_authorisation_code_phone_negative.png')

    assert 'https://start.rt.ru/?tab=main' not in page_2.get_current_url()


# TC_SAV-013 - номер теста в тест-кейсах.
@pytest.mark.positive
@pytest.mark.xfail(reason="Капча")
def test_pass_recovery_phone(web_browser):
    page = AuthPage(web_browser)

    page.recovery.click()  # забыл пароль

    page.phone.send_keys(valid_phone)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    time.sleep(10)  # задержка для учебных целей

    page.contin.click()  # кнопка "Продолжить"

    page.link_phone.click()

    page.go_click.click()  # Продолжить

    time.sleep(10)  # задержка для учебных целей

    page.rt_code.send_keys()  # первая ячейка кода

    new_pass = random  # новый пароль при восстановлении

    page.new_pass.send_keys(new_pass)

    time.sleep(10)

    page.confirm.send_keys(new_pass)  # подтверждение нового пароля

    page.save.click()

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_pass_recovery_phone.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url()


# TC_SAV-013 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
@pytest.mark.xfail(reason="Капча")
def test_pass_recovery_phone_negative(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()  # забыл пароль

    page.phone.send_keys(valid_phone)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    time.sleep(10)  # задержка для учебных целей

    page.contin.click()  # кнопка "Продолжить"

    page.link_phone.click()

    page.go_click.click()  # Продолжить

    time.sleep(10)  # задержка для учебных целей

    page.rt_code.send_keys()  # первая ячейка кода

    # new_pass = random  # новый пароль при восстановлении
    new_pass = '123@321'  # новый пароль при восстановлении

    page.new_pass.send_keys(new_pass)

    time.sleep(10)

    page.confirm.send_keys(new_pass)  # подтверждение нового пароля

    page.save.click()

    page._web_driver.save_screenshot('screenshots/test_pass_recovery_phone_negative.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in page.get_current_url()


# TC_SAV-014 - номер теста в тест-кейсах.
@pytest.mark.positive
@pytest.mark.xfail(reason="Капча")
def test_pass_recovery_email(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()   # забыл пароль

    page.email.send_keys(valid_email)

    symbols = page.captcha.get_text()  # текст капчи

    page.symbol.send_keys(symbols)  # окно капчи

    page.contin.click()   # Кнопка "Продолжить"

    page_email = web_browser.get('https://e.mail.ru/inbox/?back=1')

    element = WDW(web_browser, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span'), 'Ваш код:')

    page_email.element.click()

    element_2 = web_browser.find_element(By.TAG_NAME, 'div > p')
    for i in element_2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = '1234@ee'

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_pass_recovery_email.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url()


# TC_SAV-014 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
@pytest.mark.xfail(reason="Капча")
def test_pass_recovery_email_negative(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.email.send_keys(valid_email)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page_email = web_browser.get('https://e.mail.ru/inbox/?back=1')

    element = WDW(web_browser, 20).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span'), 'Ваш код:')

    page_email.element.click()

    element_2 = web_browser.find_element(By.TAG_NAME, 'div > p')

    for i in element_2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_pass_recovery_email.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in page.get_current_url()


# TC_SAV-015 - номер теста в тест-кейсах.
@pytest.mark.positive
@pytest.mark.xfail(reason="с Капча")
def test_pass_recovery_login(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.login.send_keys(valid_login)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page_2 = web_browser.get('https://e.mail.ru/inbox/?back=1')

    element = WDW(web_browser, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span'), 'Ваш код:'
    )
    page_2.element.click()
    element_2 = web_browser.find_element(By.TAG_NAME, 'div > p')
    for i in element_2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_pass_recovery_login.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url()


# TC_SAV-016 - номер теста в тест-кейсах.
@pytest.mark.positive
@pytest.mark.xfail(reason="Капча")
def test_pass_recovery_pers_acc(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.pa.send_keys(valid_pers_acc)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page_2 = web_browser.get('https://e.mail.ru/inbox/?back=1')

    element = WDW(web_browser, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span'), 'Ваш код:')

    page_2.element.click()

    element_2 = web_browser.find_element(By.TAG_NAME, 'div > p')

    for i in element_2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_pass_recovery_pers_acc.png')

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url()


# TC_SAV-018 - номер теста в тест-кейсах.
@pytest.mark.positive
@pytest.mark.xfail(reason='Поле ввода региона')
def test_registration_email(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('Александр')

    page.lastname.send_keys('Старикович')

    page.region.click()

    page.region.clear()

    time.sleep(3)

    page.region.send_keys('Новосибирская обл')

    page.arrow.click()  # выбор из выпадающего списка необходимо подтвердить регион

    page.email_or_phone.send_keys(valid_email)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()  # зарегистрироваться

    page.auth_code.send_keys(valid_email)

    page.get_code.click()

    page_2 = web_browser.get('https://e.mail.ru/inbox/?back=1')

    element = WDW(web_browser, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span'), 'Ваш код:')

    page_2.element.click()

    element_2 = web_browser.find_element(By.TAG_NAME, 'div > p')

    for i in element_2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_registration_email.png')

    assert 'https://start.rt.ru/?tab=main' in page.get_current_url()


# TC_SAV-018 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
@pytest.mark.xfaiёl(reason='Поле ввода региона')
def test_registration_email_negative(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('А')  # менее 2-x знаков

    page.lastname.send_keys('С')  # менее 2-x знаков

    page.region.click()

    page.region.clear()

    time.sleep(3)

    page.region.send_keys('Новосибирская обл')

    page.arrow.click()  # выбор из выпадающего списка необходимо подтвердить регион

    page.email_or_phone.click()

    page.email_or_phone.send_keys(valid_email)

    page.password.send_keys('123456ф')   # менее 8-ми знаков, присутсвует кирилица,
                                         # нет загласной и прописной латинских букв

    page.confirmation.send_keys('12345ф')  # разные пароли

    page.register.click()  # зарегистрироваться

    page.auth_code.send_keys(valid_email)

    page.get_code.click()

    page_2 = web_browser.get('https://e.mail.ru/inbox/?back=1')

    element = WDW(web_browser, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span'), 'Ваш код:')

    page_2.element.click()

    element_2 = web_browser.find_element(By.TAG_NAME, 'div > p')

    for i in element_2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_registration_email.png')

    assert 'https://start.rt.ru/?tab=main' not in page.get_current_url()


# TC_SAV-019 - номер теста в тест-кейсах.
@pytest.mark.positive
@pytest.mark.xfail(reason='Поле ввода региона')
def test_registration_phone(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('А')  # менее 2-x знаков

    page.lastname.send_keys('С')  # менее 2-x знаков

    page.region.click()

    page.region.clear()

    time.sleep(3)

    page.region.send_keys('Новосибирская обл')

    page.arrow.click()  # выбор из выпадающего списка необходимо подтвердить регион

    page.email_or_phone.click()

    page.email_or_phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_phone)

    page.get_code.click()

    page.rt_code.send_keys()

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_registration_phone.png')


    assert 'https://start.rt.ru/?tab=main' in page.get_current_url()


# TC_SAV-019 - номер теста в тест-кейсах.
@pytest.mark.negative
# @pytest.mark.parametrize
@pytest.mark.xfail(reason='Поле ввода региона')
def test_registration_phone_negative(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('А')  # менее 2-x знаков

    page.lastname.send_keys('С')  # менее 2-x знаков

    page.region.click()

    page.region.clear()

    time.sleep(3)

    page.region.send_keys('Новосибирская обл')

    page.arrow.click()  # выбор из выпадающего списка необходимо подтвердить регион

    page.email_or_phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_phone)

    page.get_code.click()

    page.rt_code.send_keys()

    time.sleep(3)

    page._web_driver.save_screenshot('screenshots/test_registration_phone_negative.png')

    assert 'https://start.rt.ru/?tab=main' not in page.get_current_url()