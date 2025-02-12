import asyncio
import ctypes
from handlers.scrapper import Scrapper
from handlers.checker import Checker
from handlers.foxkeys import FoxKeysAuth
from handlers.driver import Driver
from handlers.output import Output
from handlers.config import Config


authorized = False

'''
    Отображение действий
'''
async def show_actions():
        
    print('\nВыберите действие:')
    print('1 — Проверить никнейм')
    print('2 — Запустить авто чекер')
    print('3 — Запустить чекер по списку никнеймов')
    print('4 — Посмотреть настройки')
    print('5 — Выход')
    answer = input('· ')

    if answer == '1':
        return await check_nickname()

    elif answer == '2':
        return await start_auto_checker()

    elif answer == '3':
        return await start_nickname_list_checker()

    elif answer == '4':
        return await show_settings()

    elif answer == '5':
        raise SystemExit
    
    else:
        return await show_actions()
    

'''
    Провести авторизацию
'''
async def foxkeys_authorizate():
    global authorized

    try:
        print('\nВыберите тип авторизации на сервисе FoxKeys:')
        #print('1 — По данным')
        print('1 — ВКонтакте по данным')
        print('2 — ВКонтакте по QR коду')
        print('3 — Назад')
        answer = input('· ')

        #if answer == '1':
        #    authorized = FoxKeysAuth.data_auth()

        if answer == '1':
            authorized = FoxKeysAuth.vk_auth()

        elif answer == '2':
            authorized = FoxKeysAuth.vk_auth_qr()

        elif answer == '3':
            return await show_actions()
        
        else:
            return await foxkeys_authorizate()
    except:
        return await show_actions()


'''
    Проверить 1 никнейм
'''
async def check_nickname():
    global authorized

    try:
        if not authorized:
            await foxkeys_authorizate() # Авторизируемся

        nickname = input('· Введите никнейм для проверки: ')
        nickname_passwords = await Checker.check_nickname(nickname)

        print(f'\n→ Никнейм: {nickname}')
        print(f'→ Пароли: {" ".join(nickname_passwords)}')
    finally:
        return await show_actions()


'''
    Запуск авто чекера
'''
async def start_auto_checker():
    global authorized

    try:
        if not authorized:
            await foxkeys_authorizate() # Авторизируемся

        await Checker.auto_checker()
    finally:
        return await show_actions()


'''
    Запуск чекера по никнеймам
'''
async def start_nickname_list_checker(nicknames_file = 'data/nicknames.txt'):
    global authorized

    try:
        if not authorized:
            await foxkeys_authorizate() # Авторизируемся

        file_answer = input('· Введите путь к файлу с никнеймами (по умолчанию data/nicknames.txt): ')
        if file_answer:
            nicknames_file = file_answer

        with open(nicknames_file, 'r') as f:
            data = f.read().splitlines()
        dict = {nicknames_file : data}

        passwords_data = await Checker.check_nicknames(dict)
        Output.to_json_file(passwords_data)
    finally:
        return await show_actions()


'''
    Настройка параметров конфига
'''
async def configure_settings():

    try:
        config = Config.get()
        
        answer = input('· Время между циклами авто чекера (в минутах): ')
        config["checker_settings"]["auto_checker_delay"] = int(answer) if int(answer) else 15
        
        answer = input('· Путь к выходному файлу: ')
        config["checker_settings"]["output_file_path"] = answer if answer else "output/checked.json"
        
        answer = input('· Компилировать дубликаты паролей в количество (выводятся самыми первыми) [y/n]: ')
        config["checker_settings"]["checker_compile_into_quantity"] = True if answer == 'y' or answer == 'Y' else False
        
        answer = input('· Убрать из поиска COMBO (логи) сервера [y/n]: ')
        config["checker_settings"]["checker_remove_combo_logs"] = True if answer == 'y' or answer == 'Y' else False
        
        answer = input('· Автоматически расшифровывать хеши по базе [y/n]: ')
        config["checker_settings"]["checker_auto_decrypt_hashes"] = True if answer == 'y' or answer == 'Y' else False
        
        answer = input('· Вывод результатов с БД за 2022-2024 годы [y/n]: ')
        config["checker_settings"]["checker_results_from_2022_2024"] = True if answer == 'y' or answer == 'Y' else False
        
        answer = input('· Макс. время ожидание на действие в драйвере в минутах (если слабый Wi-Fi, ставьте значение больше): ')
        config["other_settings"]["driver_max_wait"] = int(answer) if int(answer) else 30

        Config.update(config)
        print('Настройка конфига завершена. Изменения были применены')
        
    except Exception as e:
        print(f'Настройка провалилась, возможно вы неправильно ввели значение(-я): {e}')

'''
    Просмотр настроек
'''
async def show_settings(nicknames_file = 'data/nicknames.txt'):
    
    config = Config.get()

    print(f'\nНастройки чекера:')
    print(f'→ Время между циклами авто чекера (в минутах): {config["checker_settings"]["auto_checker_delay"]}')
    print(f'→ Путь к выходному файлу: {config["checker_settings"]["output_file_path"]}')
    print(f'→ Компилировать дубликаты паролей в количество (выводятся самыми первыми): {config["checker_settings"]["checker_compile_into_quantity"]}')
    print(f'→ Убрать из поиска COMBO (логи) сервера: {config["checker_settings"]["checker_remove_combo_logs"]}')
    print(f'→ Автоматически расшифровывать хеши по базе: {config["checker_settings"]["checker_auto_decrypt_hashes"]}')
    print(f'→ Вывод результатов с БД за 2022-2024 годы: {config["checker_settings"]["checker_results_from_2022_2024"]}')
    print(f'Прочие настройки:')
    print(f'→ Макс. время ожидание на действие в драйвере в минутах (если слабый Wi-Fi, ставьте значение больше): {config["other_settings"]["driver_max_wait"]}')

    print('\nВыберите действие:')
    print('1 — Настроить параметры конфига')
    print('2 — Назад')
    answer = input()

    if answer == '1':
        await configure_settings()
    elif answer == '2':
        return await show_actions()

    return await show_actions()



if __name__ == "__main__":

    print(
        '\n'
        '█▀▀ █▀▀█ █─█ █─█ █▀▀ █──█ █▀▀ █▀▀▄ █▀▀█ ▀▀█▀▀\n' 
        '█▀▀ █──█ ▄▀▄ █▀▄ █▀▀ █▄▄█ ▀▀█ █▀▀▄ █──█ ──█──\n' 
        '▀── ▀▀▀▀ ▀─▀ ▀─▀ ▀▀▀ ▄▄▄█ ▀▀▀ ▀▀▀─ ▀▀▀▀ ──▀──123123123\n'
        '┕ by a.lexey')
    ctypes.windll.kernel32.SetConsoleTitleA(b"FoxKeys Bot | by a.lexey")
    
    asyncio.run(show_actions())