import json


class Config():

    '''
        Стандартная структура конфига
    '''
    def default_config():
        return {
            "checker_settings": {
                "auto_checker_delay": 15,
                "output_file_path": "output/checked.json",
                "checker_compile_into_quantity": True,
                "checker_remove_combo_logs": False,
                "checker_auto_decrypt_hashes": True,
                "checker_results_from_2022_2024": False,
            },
            "other_settings": {
                "driver_max_wait": 30,
            }
        }
    
    
    '''
        Получение конфига
    '''
    def get():
        # Если конфиг существует - открываем его
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
        # Иначе создаём его со стандартной структурой
        except FileNotFoundError:
            with open('config.json', 'w') as f:
                json.dump(Config.default_config(), f)
            config = Config.get()
        finally:
            return config
    

    '''
        Обновление конфига
    '''
    def update(new_config):
        with open('config.json', 'w') as f:
            json.dump(new_config, f)