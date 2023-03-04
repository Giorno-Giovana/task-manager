"""Указание путей для корректного импорта модулей"""
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

"""Импорт адаптеров"""
from adapters import *
import datetime


"""Пишем текущее время в файл /data/test"""
with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
    file.write(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'\n')
"""Отправляем сообщение телеграм"""
Telegram.send('Сообщение телеграм отправлено')
"""Отправляем сообщение E-mail"""
Mail.send('Сообщение E-mail отправлено')