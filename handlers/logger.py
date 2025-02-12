from datetime import datetime



class Logger:


    '''
        Логгирование в консоль
    '''
    def log(message):
        now = datetime.now()
        print(f'[{now.strftime("%H:%M:%S")}] {message}')