import requests

from src.parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """
        :param keyword: слово для поиска по вакансиям на ХХ.ру
        :return: список вакансий пришедший с АПИ ХХ.р
        """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
