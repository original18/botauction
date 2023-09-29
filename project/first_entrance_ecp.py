from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
import time

load_dotenv()
login = os.getenv("login")
password = os.getenv("password")


def enrance_to_main_ecp(driver):
    btn_gos = driver.find_elements(By.CLASS_NAME, "x-btn-text")
    btn_gos[0].click()
    print("нАЖАТЫ ГОСУСЛУГИ ")
    time.sleep(10)
    if driver.current_url == 'https://etp.roseltorg.ru/supplier/auction/index':
        pass
    else:
        login_input = driver.find_element(By.ID, "login")
        print("Вводим логин, пароль")
        try:
            login_input.is_displayed() and login_input.is_enabled()
            login_input.send_keys(Keys.CONTROL + "a")
            login_input.send_keys(Keys.DELETE)
            login_input.send_keys(login)
            time.sleep(10)
        except Exception:
            print("Пароль некликабельный, идем дальше")
        finally:
            password_input = driver.find_element(By.ID, "password")
            password_input.send_keys(Keys.CONTROL + "a")
            password_input.send_keys(Keys.DELETE)
            password_input.send_keys(password)
            driver.find_element(By.CLASS_NAME, "plain-button_wide").click()
            time.sleep(10)
            print("пароль ввели")
            driver.find_element(By.CLASS_NAME, "plain-button-inline").click()
            time.sleep(10)
            print("Вход по эцп выбран")
            time.sleep(10)
