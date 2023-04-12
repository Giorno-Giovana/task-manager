from adapter import Adapter


class Mail(Adapter):
    """Адаптер для E-mail"""

    def send(message):
        """Отправка сообщения"""
        with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
            file.write(message + '\n')
