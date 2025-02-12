from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import random

#import undetected_chromedriver as uc

class Driver():

    _driver = None


    '''
        Создание Chrome драйвера
    '''
    def create_driver():

        # Получение рандомного юзер агента
        def random_user_agent():
            with open("data/user_agents.txt") as inp:
                lines = inp.readlines()
            return random.choice(lines).strip()


        options = webdriver.ChromeOptions()
        options.page_load_strategy = "eager"
        options.add_argument("--start-maximized")
        #options.add_argument("--headless=new")
        options.add_argument("--disable-images")
        options.add_argument("--blink-settings=imagesEnabled=false")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(f"--user-agent={random_user_agent()}")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-in-process-stack-traces")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--output=/dev/null")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        service = Service()

        driver = webdriver.Chrome(service=service, options=options)
        #driver = uc.Chrome(options=options)
        return driver
    

    '''
        Загрузка Cookie в браузер
    '''
    def load_cookies(driver, cookies_file):
        try:
            with open(cookies_file, 'r', encoding='utf-8') as file:
                cookies = json.load(file)
            
            for cookie in cookies:
                if 'sameSite' in cookie and cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                    cookie.pop('sameSite')
                if 'secure' in cookie and not isinstance(cookie['secure'], bool):
                    cookie['secure'] = bool(cookie['secure'])
                driver.add_cookie(cookie)
            driver.refresh()
        except Exception as e:
            print(f"Ошибка загрузки куки: {e}")
            

    '''
        Получение драйвера браузера
    '''
    def get_driver():
        if Driver._driver is None:
            Driver._driver = Driver.create_driver()
        return Driver._driver