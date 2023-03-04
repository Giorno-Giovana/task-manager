from abc import ABC, abstractmethod


class Adapter(ABC):
    """Адаптеры для мессенджеров"""
    """Если метод у дочернего класса отсутсвует, то выполняется этот метод"""

    @abstractmethod
    def send(message):
        with open('/task-manager/data/test', 'a', encoding='utf-8') as file:
            file.write('Сообщение: "' + message + '" не отправлено\n')