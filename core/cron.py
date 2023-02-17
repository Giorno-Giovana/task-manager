import time

if __name__ == "__main__":
    while 1>0:
        # Запускаем файл 'main.py' каждую минуту
        exec(open('main.py','r').read())
        time.sleep(60)