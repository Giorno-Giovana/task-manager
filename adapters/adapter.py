class Adapter():
    """Адаптеры для мессенджеров"""
    """Если метод у дочернего класса отсутсвует, то выполняется этот метод"""
    def send(message):
        with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
            file.write('Сообщение: "'+ message +'" не отправлено\n')
        return


class Telegram(Adapter):
    """Адаптер для Telegram"""
    """Метод  send пишет в файл /data/test отправленное сообщение"""
    def send(message):
        """Отправка сообщения"""
        with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
            file.write(message+'\n')
        return


class Email(Adapter):
    """Адаптер для E-mail"""
    """Метод send отсутствует, выполняется метод родительского класса"""
    def wend(message):
        return

# Telegram.send('Hello')
# import requests
#
# def send_telegram(text: str):
#     token = "ТУТ_ВАШ_ТОКЕН_КОТОРЫЙ_ВЫДАЛ_BotFather"
#     url = "https://api.telegram.org/bot"
#     channel_id = "@ИМЯ_КАНАЛА"
#     url += token
#     method = url + "/sendMessage"
#
#     r = requests.post(method, data={
#         "chat_id": channel_id,
#         "text": text
#     })
#
#     if r.status_code != 200:
#         raise Exception("post_text error")
