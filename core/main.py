"""Импорт адаптеров"""
from adapters import adapter as ad
import datetime
"""Пишем текущее время в файл /data/test"""
with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
    file.write(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'\n')
"""Отправляем сообщение телеграм"""
ad.Telegram.send('Сообщение телеграм отправлено')
"""Отправляем сообщение E-mail"""
ad.Email.send('Сообщение E-mail отправлено')