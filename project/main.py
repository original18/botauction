from first_entrance_ecp import enrance_to_main_ecp

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pickle
import time

load_dotenv()

url = os.getenv("url")
executable_path = os.getenv("executable_path")
ex_path = os.getenv("ex_path")
options = webdriver.ChromeOptions()
options.add_extension('./1.2.13_0.crx')
options.add_argument("--disable-blink-features=AutomationControlled")
options.binary_location = os.getenv("binary_location")
options.add_argument("--no-sandbox")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--ignore-certificate-errors')
options.add_argument(f"--user-data-dir={ex_path}")
driver = webdriver.Chrome(
    executable_path=executable_path,
    options=options
)


def close_alert():
    try:
        clock_alert_btn = driver.find_element(By.CLASS_NAME, "x-tool-close")
        clock_alert_btn.click()
        print("Уведомление закрыл, я на главной")
    except Exception as e:
        print(e)
    finally:
        print("я на главной")


def main():
    try:
        driver.get(url=url)
        time.sleep(5)
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(10)
        if os.path.exists("cookies"):
            for cookie in pickle.load(open("cookies", "rb")):
                driver.add_cookie(cookie)
            driver.refresh()
            print("зашел с куками")
            time.sleep(10)

        else:
            enrance_to_main_ecp(driver)
            pickle.dump(driver.get_cookies(), open("cookies", "wb"))
            driver.refresh()
            time.sleep(60)
            close_alert()
            time.sleep(10)
        print("Работаем дальше")
        lk_btns = driver.find_elements(By.CLASS_NAME, "x-btn-text-icon")
        lk_btns[3].click()
        time.sleep(10)
        print("выбраны заявки")

    except Exception as ex:
        print(ex)
    finally:
        driver.delete_all_cookies()
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
