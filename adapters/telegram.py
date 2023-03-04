from adapters.adapter import Adapter


class Telegram(Adapter):
    """Адаптер для Telegram"""
    """Метод  send пишет в файл /data/test отправленное сообщение"""

    def send(message):
        """Отправка сообщения"""
        with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
            file.write(message + '\n')
