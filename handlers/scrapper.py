from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from handlers.driver import Driver
from handlers.logger import Logger
from handlers.config import Config
import time

class Scrapper():
    config = Config.get()

    # Скраппинг никнеймов с MusteryWorld
    def scrap_musteryworld(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://musteryworld.net/"
            ip = "mc.musteryworld.net"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.payment-id'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.payment-id')
            for item in purchase_items:
                nickname = item.find_elements(By.CSS_SELECTOR, 'div.player')[0].text.replace('─','').replace('*','').strip()
                product = item.find_elements(By.CSS_SELECTOR, 'div.title')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов со SpookyTime
    def scrap_spookytime(max_wait = config["other_settings"]["driver_max_wait"]):
    
        try:
            nicknames = {}
            url = "https://shop.spookytime.net/"
            ip = "spookytime.net"
            Logger.log(f'Извлечение никнеймов {url}')
            
            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.owl-item'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                nickname_elem = item.find_elements(By.CSS_SELECTOR, 'p.mb-0')[0]
                nickname = driver.execute_script("return arguments[0].childNodes[arguments[0].childNodes.length - 1].textContent;", nickname_elem).strip()
                product = item.find_elements(By.CSS_SELECTOR, 'h5.mb-0')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
    

    # Скраппинг никнеймов с AresMine
    def scrap_aresmine(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://aresmine.ru/"
            ip = "hot.aresmine.me"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.last-purchase-card_root__kfg2W'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.last-purchase-card_root__kfg2W')
            for item in purchase_items:
                nickname = item.find_elements(By.CSS_SELECTOR, 'span.typography_root__e6f5j')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, 'span.typography_root__e6f5j')[1].get_attribute('title').strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с MineLord
    def scrap_minelord(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://minelord.ru/"
            ip = "mr.minelord.ru"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.title-last-product'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.last-product')
            for item in purchase_items:
                nickname = item.find_elements(By.CSS_SELECTOR, 'div.nick-last-product')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, 'div.title-last-product')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с MineLandy
    def scrap_minelandy(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://minelandy.com/"
            ip = "mr.minelandy.com"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.title'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.payment-id')
            for item in purchase_items:
                nickname = item.find_elements(By.CSS_SELECTOR, 'div.player')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, 'div.title')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        
        
    # Скраппинг никнеймов с FunnyGame
    def scrap_funnygame(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://funnygame.su/"
            ip = "play.mcfunny.net"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.payment-id'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.payment-id')
            for item in purchase_items:
                nickname = item.find_elements(By.CSS_SELECTOR, 'div.player')[0].text.replace('─','').replace('*','').strip()
                product = item.find_elements(By.CSS_SELECTOR, 'div.title')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        
        
    # Скраппинг никнеймов с 3b3t
    def scrap_3b3t(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://shop.3b3t.ru/"
            ip = "mc.3b3t.fun"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.owl-item'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                nickname_elem = item.find_elements(By.CSS_SELECTOR, 'p.mb-0')[0]
                nickname = driver.execute_script("return arguments[0].childNodes[arguments[0].childNodes.length - 1].textContent;", nickname_elem).strip()
                product = item.find_elements(By.CSS_SELECTOR, 'h5.mb-0')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        
    
    # Скраппинг никнеймов с LuckyDayz
    def scrap_luckydayz(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://www.luckydayz.ru/"
            ip = "mc.luckydayz.ru"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.online_purchases_game'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.online_purchases_game')
            for item in purchase_items:
                data = item.get_attribute('data-original-title')
                nickname = data.split('<br>')[0].split(' ')[1].strip()
                product = data.split('<br>')[1].split(' ')[1].strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с FastMC
    def scrap_fastmc(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://fast-mc.ru/"
            ip = "mc.fast-mc.ru"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)
            driver.execute_script("window.scrollTo(0, 1080)")

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.owl-item'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                nickname = item.find_elements(By.TAG_NAME, 'small')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, 'p.mb-0')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с ToffiCraft
    def scrap_tofficraft(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://tofficraft.ru/"
            ip = "toffi.top"
            Logger.log(f'Извлечение никнеймов {url}')
            
            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.last_purchases'))
            )

            last_purchases = driver.find_elements(By.CSS_SELECTOR, '.last_purchases')[0]
            purchase_items = last_purchases.find_elements(By.CSS_SELECTOR, '.box')
            for item in purchase_items:
                nickname = item.find_elements(By.CSS_SELECTOR, '.name')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, '.product')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с ArcherGrief
    def scrap_archergrief(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://www.archergrief.pw/"
            ip = "mc.archergrief.pw"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)
            driver.execute_script("window.scrollTo(0, 1080)")

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.owl-item'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                nickname = item.find_elements(By.TAG_NAME, 'small')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, 'p.mb-0')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с MoniDays
    def scrap_monidays(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://monidays.net/"
            ip = "play.monidays.net"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)
            driver.execute_script("window.scrollTo(0, 1080)")

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.owl-item'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                nickname = item.find_elements(By.TAG_NAME, 'small')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, 'p.mb-0')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с SkyBars
    def scrap_skybars(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://skybars.me/"
            ip = "play.skybars.me"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.owl-item'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                try:
                    nickname = item.find_elements(By.CSS_SELECTOR, '.product-name')[0].text.strip()
                    product = item.find_elements(By.CSS_SELECTOR, '.product-title')[0].text.strip()
                except:
                    pass
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с GrandGrief
    def scrap_grandgrief(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://grandgrief.pw/"
            ip = "mc.grandgrief.pw"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.owl-item'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                nickname = item.find_elements(By.TAG_NAME, 'small')[0].text.strip()
                product = item.find_elements(By.CSS_SELECTOR, 'p.mb-0')[0].get_attribute('title').strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов с HoweMine
    def scrap_howemine(max_wait = config["other_settings"]["driver_max_wait"]):

        try:
            nicknames = {}
            url = "https://www.howemine.su/"
            ip = "mc.howemine.su"
            Logger.log(f'Извлечение никнеймов {url}')

            driver = Driver.get_driver()
            driver.get(url)

            WebDriverWait(driver, max_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h5.mb-0'))
            )

            purchase_items = driver.find_elements(By.CSS_SELECTOR, '.owl-item')
            for item in purchase_items:
                nickname_elem = item.find_elements(By.CSS_SELECTOR, 'p.mb-0')[0]
                nickname = driver.execute_script("return arguments[0].childNodes[arguments[0].childNodes.length - 1].textContent;", nickname_elem).strip()
                product = item.find_elements(By.CSS_SELECTOR, 'h5.mb-0')[0].text.strip()
                if nickname:
                    nicknames[nickname] = {}
                    nicknames[nickname]["product"] = product
            return {ip : nicknames}
        except:
            return {}
        

    # Скраппинг никнеймов со всех доступных серверов
    def scrap_all():
        s = Scrapper
        return { 
            **s.scrap_musteryworld(),  
            **s.scrap_spookytime(),  
            **s.scrap_aresmine(),  
            **s.scrap_minelord(), 
            **s.scrap_minelandy(), 
            **s.scrap_funnygame(), 
            **s.scrap_3b3t(),
            **s.scrap_luckydayz(),
            **s.scrap_fastmc(),
            **s.scrap_tofficraft(),
            **s.scrap_archergrief(),
            **s.scrap_monidays(),
            **s.scrap_skybars(),
            **s.scrap_grandgrief(),
            **s.scrap_howemine(),
        }
        