from abc import ABC, abstractmethod


class FileWorker(ABC):
    """
    Создаем абстрактный класс FileWorker, предназначен для шаблонизации классов,
    осуществляющих работу с файлами
    """
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        """
        загрузка вакансий
        """
        pass

    @abstractmethod
    def write_vacancies(self, vacancies):
        """
        запись вакансий
        """
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        """
        добавление какансий
        """
        pass

    @abstractmethod
    def del_vacancy_full(self, vacancy):
        """
        удаление вакансии
        """
        pass

    @abstractmethod
    def del_vacancy_one(self, vacancy):
        """
        удаление вакансий
        """
        pass
