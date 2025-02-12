import json
from handlers.config import Config


class Output:
    config = Config.get()
    
    '''
        Запись содержимого в json со слиянием словарей
    '''
    def to_json_file(text, file=config["checker_settings"]["output_file_path"]):
        try:
            # Проверка, существует ли файл
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    resources = json.load(f)
            # Если не существует - создаём
            except FileNotFoundError:
                resources = {}

            # Записываем данные в файл. Данные слияния текущего словаря и нового полученного
            with open(file, 'w', encoding='utf-8') as f:
                json.dump({**resources, **text}, f, ensure_ascii=False, indent=4)

            print(f'Данные были сохранены/дополнены в JSON файл {file}')
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
            print(f"Чтобы не потерять данные, выводим их в консоль: \n{text}")