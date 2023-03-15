import datetime
"""Импорт адаптеров"""
from adapters import *


"""Пишем текущее время в файл /data/test"""
with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
    file.write(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'\n')
"""Отправляем сообщение телеграм"""
Telegram.send('Сообщение Telegram отправлено')
"""Отправляем сообщение E-mail"""
Mail.send('Сообщение E-mail отправлено')