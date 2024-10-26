from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Создаем абстрактный класс Parser, Parser является родительским классом, от которого так же могут
    наследовваться другие парсеры
    """
    @abstractmethod
    def load_vacancies(self, keyword):
        pass
