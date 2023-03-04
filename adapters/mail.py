from adapters.adapter import Adapter


class Mail(Adapter):
    """Адаптер для E-mail"""
    """Метод  send пишет в файл /data/test отправленное сообщение"""
    pass
    # def send(message):
    #     """Отправка сообщения"""
    #     with open('../data/test', 'a', encoding='utf-8') as file:
    #         file.write(message + '\n')
