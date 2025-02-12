from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from handlers.driver import Driver
from handlers.config import Config



class FoxKeysAuth:
    config = Config.get()

    ''' 
        Авторизация по данным FoxKeys
    '''
    def data_auth(max_wait = config["other_settings"]["driver_max_wait"], min_wait = 3):
        try:
            driver = Driver.get_driver()
            url = "https://foxkeys.io/login"
            driver.get(url)
            
            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.NAME, 'username'))
            )
            driver.find_element(By.NAME, 'username').click()
            driver.find_element(By.NAME, 'username').send_keys('testing')

            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'div.recaptcha-checkbox-border'))
            )
            driver.find_element(By.TAG_NAME, 'div.recaptcha-checkbox-border').click()
            

        except:
            print("Время на ожидание вышло.")
            return False


    ''' 
        Авторизация через ВКонтакте по данным
    '''
    def vk_auth(max_wait = config["other_settings"]["driver_max_wait"], min_wait = 3):
        try:
            driver = Driver.get_driver()
            url = "https://foxkeys.io/login"
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.btn-vk'))
            )
            driver.find_element(By.CSS_SELECTOR, '.btn-vk').click()

            # Дожидаемся загрузки страницы ВК авторизации
            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.vkuiText'))
            )

            # Закрываем всплывающее окно, если открылось
            try:
                WebDriverWait(driver, min_wait).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.vkuiModalCardBase__dismiss'))
                )
                driver.find_element(By.CSS_SELECTOR, '.vkuiModalCardBase__dismiss').click()
            except:
                pass

            # Запрашивание страны номера телефона
            try:
                phone_country = input('· Введите полное название страны вашего номера (Enter чтобы пропустить и использовать исходя из вашего местоположения): ')
                if phone_country != '':
                    driver.find_element(By.CSS_SELECTOR, '.PhoneInput-module_phoneInput_numberIconInner__saRYB').click()
                    driver.find_element(By.CSS_SELECTOR, '.CountryList-module_countryList__searchInput__78KEC').send_keys(phone_country)
                    driver.find_elements(By.CSS_SELECTOR, '.CountryList-module_countryList__listItem__bflkV')[0].click()
            except:
                print('Введённая страна не найдена')
                return False

            # Запрашивание номера телефона
            try:
                phone_number = input('· Введите номер телефона ВК (без кода номера страны): ')
                driver.find_element(By.CSS_SELECTOR, '.vkuiText').send_keys(phone_number)
                driver.find_element(By.CSS_SELECTOR, '.vkuiButton--mode-primary').click()
            except:
                print('Введён неверный номер телефона')
                return False
            
            # Запрашивание пароля для входа
            try:
                WebDriverWait(driver, min_wait).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.vkc__TextField__input_password'))
                )
                password = input('· Введите пароль: ')
                driver.find_element(By.CSS_SELECTOR, '.vkc__TextField__input_password').send_keys(password)
                driver.find_element(By.CSS_SELECTOR, '.vkuiButton').click()
            except:
                print('Введён неверный пароль')
                return False

            # Проверка на запрашивание капчи
            try:
                WebDriverWait(driver, min_wait).until(
                    EC.presence_of_all_elements_located((By.ID, 'captcha-text'))
                )
                print('ВКонтакте заметил подозрительную активность с этого айпи адреса. Попробуйте войти позже или повторите попытку со включённым ВПН.')
                return False
            except:
                pass

            # Запрашивание смс кода для входа
            try:
                WebDriverWait(driver, max_wait).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.vkc__TextField__codeInput'))
                )
                
                code = input('· Введите код из уведомления: ')
                driver.find_element(By.CSS_SELECTOR, '.vkc__TextField__codeInput').send_keys(code)
                driver.find_element(By.CSS_SELECTOR, '.vkuiButton__in').click()
            except:
                print('Введён неверный код')
                return False
            
            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.vkc__Button__primary'))
            )
            WebDriverWait(driver, max_wait).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.vkc__Button__primary'))
            )
            driver.find_element(By.CSS_SELECTOR, '.vkc__Button__primary').click()

            try:
                WebDriverWait(driver, max_wait).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".header-profile"))
                )
                print('Успешная авторизация!')
                return True

            except TimeoutException:
                print("Время на авторизацию вышло.")
                return False
        except:
            print("Время на ожидание вышло.")
            return False


    ''' 
        Авторизация через ВКонтакте по QR коду
    '''
    def vk_auth_qr(max_auth_time = 90, max_wait = config["other_settings"]["driver_max_wait"], min_wait = 3):
        try:
            driver = Driver.get_driver()
            url = "https://foxkeys.io/login"
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.btn-vk'))
            )
            driver.find_element(By.CSS_SELECTOR, '.btn-vk').click()

            # Дожидаемся загрузки страницы ВК авторизации
            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.vkc__QRCode__image'))
            )

            # Закрываем всплывающее окно, если открылось
            try:
                WebDriverWait(driver, min_wait).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.vkuiModalCardBase__dismiss'))
                )
                driver.find_element(By.CSS_SELECTOR, '.vkuiModalCardBase__dismiss').click()
            except:
                pass

            qr_svg = driver.find_element(By.CSS_SELECTOR, '.vkc__PromoBox__qrPromoContainer')
            png_data = qr_svg.screenshot_as_png

            # Сохранить PNG-изображение
            with open("qr.png", "wb") as file:
                file.write(png_data)

            print('Отсканируйте QR-код с файла qr.png для авторизации и подтвердите вход в приложении VK')

            # Ждём пока сменится адрес сайта, что означает успешную авторизацию
            WebDriverWait(driver, max_auth_time).until(EC.url_to_be("https://foxkeys.io/index"))
            print('Успешная авторизация')
            return True
            
        except:
            print("Время на ожидание вышло.")
            return False