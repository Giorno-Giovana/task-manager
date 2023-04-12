from abc import ABC, abstractmethod


class Adapter(ABC):
    """Адаптеры для мессенджеров"""
    """Если метод у дочернего класса отсутсвует, то выполняется этот метод"""

    @abstractmethod
    def send(message):
        pass
