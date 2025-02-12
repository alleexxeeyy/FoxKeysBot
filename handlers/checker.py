import asyncio
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from handlers.driver import Driver
from handlers.logger import Logger
from handlers.scrapper import Scrapper
from handlers.output import Output
from handlers.config import Config


class Checker:
    config = Config.get()

    '''
        Проверка одного никнейма в чекере
    '''
    async def check_nickname(nickname, max_wait = config["other_settings"]["driver_max_wait"], min_wait = 3):
        try:
            # Заходим на чекер
            driver = Driver.get_driver()
            url = "https://foxkeys.io/vipchecker"
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_element_located((By.NAME, 'nickname'))
            )

            WebDriverWait(driver, max_wait).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.form-check-input'))
            )
            checkboxes = driver.find_elements(By.CSS_SELECTOR, '.form-check-input')

            
            # Выставляем в чекере параметры исходя из конфига
            try:
                actions = ActionChains(driver)
                config = Config.get()
                if config["checker_settings"]["checker_compile_into_quantity"]:
                    actions.move_to_element(checkboxes[0]).click().perform()
                if config["checker_settings"]["checker_remove_combo_logs"]:
                    actions.move_to_element(checkboxes[1]).click().perform()
                if config["checker_settings"]["checker_auto_decrypt_hashes"]:
                    actions.move_to_element(checkboxes[3]).click().perform()
                if config["checker_settings"]["checker_results_from_2022_2024"]:
                    actions.move_to_element(checkboxes[4]).click().perform()
            except:
                pass

            passwords = [] # Словарь, содержащий пароли никнейма
            Logger.log(f'Проверка никнейма {nickname}')

            # Находим и вписываем никнейм в поле ввода чекера
            nickname_input = driver.find_element(By.NAME, 'nickname')
            nickname_input.click()
            nickname_input.clear()
            nickname_input.send_keys(nickname)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()

            await asyncio.sleep(5) # Ждём некоторое время, пока загрузятся все новые пароли

            # Если всплывает сообщение о том, что ничего не было найдено
            try:
                WebDriverWait(driver, min_wait).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.alert-warning'))
                )
                # Возвращаем пустой массив
                return []
            except:
                pass

            # Получаем список всех паролей
            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'tbody'))
            )
            list_container = driver.find_element(By.TAG_NAME, 'tbody')

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
            )
            list_items = list_container.find_elements(By.TAG_NAME, 'tr')
            
            # Проходимся по каждому выданному паролю в списке
            for list_item in list_items:
                WebDriverWait(driver, max_wait).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'td'))
                )
                item_content = list_item.find_elements(By.TAG_NAME, 'td')

                # Извлекаем пароль и добавляем его в массив
                if item_content:
                    # Проверка, если элемент контента не имеет дочерних элементов (чтобы пропустить зашифрованные пароли)
                    if not item_content[2].find_elements(By.CSS_SELECTOR, "*"):
                        # Форматируем пароль
                        password = re.sub(r'[ЁёА-я]', '', item_content[2].text).strip()
                        if password and password != '':
                            # Добавляем пароль в массив паролей
                            passwords.append(password)

            # Если у этого никнейма есть пароли, то возвращаем их
            if passwords:
                return passwords
            
        except Exception as e:
            print(e)
            pass


    ''' 
        Проверка словаря никнеймов в чекере 
    '''
    async def check_nicknames(data_dict, max_wait = config["other_settings"]["driver_max_wait"], min_wait = 3):
    
        # Заходим на чекер
        driver = Driver.get_driver()
        url = "https://foxkeys.io/vipchecker"
        driver.get(url)

        WebDriverWait(driver, max_wait).until(
            EC.presence_of_element_located((By.NAME, 'nickname'))
        )

        WebDriverWait(driver, max_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.form-check-input'))
        )
        checkboxes = driver.find_elements(By.CSS_SELECTOR, '.form-check-input')

        
        # Выставляем в чекере параметры исходя из конфига
        try:
            actions = ActionChains(driver)
            config = Config.get()
            if config["checker_settings"]["checker_compile_into_quantity"]:
                actions.move_to_element(checkboxes[0]).click().perform()
            if config["checker_settings"]["checker_remove_combo_logs"]:
                actions.move_to_element(checkboxes[1]).click().perform()
            if config["checker_settings"]["checker_auto_decrypt_hashes"]:
                actions.move_to_element(checkboxes[3]).click().perform()
            if config["checker_settings"]["checker_results_from_2022_2024"]:
                actions.move_to_element(checkboxes[4]).click().perform()
        except:
            pass


        # Перебираем каждый сервер
        for server in data_dict:
            Logger.log(f'Проверка никнеймов {server}')

            # Перебираем каждый никнейм в сервере
            for nickname in data_dict[server]:
                try:
                    passwords = [] # Массив, содержащий пароли текущего никнейма в итерации

                    # Находим и вписываем никнейм в поле ввода чекера
                    nickname_input = driver.find_element(By.NAME, 'nickname')
                    nickname_input.click()
                    nickname_input.clear()
                    nickname_input.send_keys(nickname)
                    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

                    await asyncio.sleep(min_wait) # Ждём некоторое время, пока загрузятся все новые пароли

                    # Если всплывает сообщение о том, что ничего не было найдено
                    try:
                        WebDriverWait(driver, min_wait).until(
                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.alert-warning'))
                        )
                        continue
                    except:
                        pass

                    # Получаем список всех паролей
                    WebDriverWait(driver, max_wait).until(
                        EC.presence_of_all_elements_located((By.TAG_NAME, 'tbody'))
                    )
                    list_container = driver.find_element(By.TAG_NAME, 'tbody')

                    WebDriverWait(driver, max_wait).until(
                        EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
                    )
                    list_items = list_container.find_elements(By.TAG_NAME, 'tr')
                    
                    # Проходимся по каждому выданному паролю в списке
                    for list_item in list_items:
                        WebDriverWait(driver, max_wait).until(
                            EC.presence_of_all_elements_located((By.TAG_NAME, 'td'))
                        )
                        item_content = list_item.find_elements(By.TAG_NAME, 'td')

                        # Извлекаем пароль и добавляем его в массив
                        if item_content:
                            # Проверка, если элемент контента не имеет дочерних элементов (чтобы пропустить зашифрованные пароли)
                            if not item_content[2].find_elements(By.CSS_SELECTOR, "*"):
                                # Форматируем пароль
                                password = re.sub(r'[ЁёА-я]', '', item_content[2].text).strip()
                                if password:
                                    # Добавляем пароль в массив паролей
                                    passwords.append(password)

                    # Если у этого никнейма есть пароли, то добавляем в словарь
                    if passwords:
                        data_dict[server][nickname]["passwords"] = passwords

                except:
                    pass

            # Очищаем словарь от никнеймов без паролей
            for nickname in list(data_dict[server]):
                if not "passwords" in data_dict[server][nickname]:
                    del data_dict[server][nickname]

        return data_dict
    

    ''' 
        Автоматический чекер (парсит и проверяет все имена с периодичностью в минутах)
    '''
    async def auto_checker():
        config = Config.get()
        delay = config["checker_settings"]["auto_checker_delay"]
        delay_sec = delay * 60

        while True:
            nicknames = Scrapper.scrap_all()
            passwords_data = await Checker.check_nicknames(nicknames)
            Output.to_json_file(passwords_data)

            Logger.log(f'Ждём {delay} мин.')
            await asyncio.sleep(delay_sec)
