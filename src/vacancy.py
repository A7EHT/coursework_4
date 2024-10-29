class Vacancy:
    """
    Класс Vacancy, для работы с вакансиями
    """
    def __init__(self, name, url, salary_from, salary_to, currency, description):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.check_data_int()
        self.check_data_str()

    def __str__(self):
        return (f'============================================================'
                f'\nВакансия: {self.name}\n'
                f'Описание: {self.description.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                f'Зарплата: {self.salary_from} - {self.salary_to} - {self.currency}\n'
                f'Ссылка на страницу вакансии: {self.url}\n'
                f'============================================================')

    @classmethod
    def vacancies_list(cls, vacancies_list):
        """
        Класс-метод для создания ЭК из словарей формата Response, получаемых с АПИ ХХ.ру
        """
        vacan_list = []
        for i in vacancies_list:
            vac_name = i["name"]
            vac_url = i["url"]
            if i.get("salary"):
                salary_from = cls.check_data_int(i.get("salary").get("from"))
                salary_to = cls.check_data_int(i.get("salary").get("to"))
                currency = cls.check_data_str(i.get("salary").get("currency"))
            else:
                salary_from = 0
                salary_to = 0
                currency = ""
            vac_description = cls.check_data_str(i["snippet"]["requirement"])
            vacancy_obj = cls(vac_name, vac_url, salary_from, salary_to, currency, vac_description)  # Vacancy == cls
            vacan_list.append(vacancy_obj)
        return vacan_list

    def __lt__(self, other):
        if type(other) == int:
            return self.salary_from < other
        else:
            return self.salary_from < other.salary_from

    def __le__(self, other):
        if type(other) == int:
            return self.salary_from <= other
        else:
            return self.salary_from <= other.salary_from

    def __eq__(self, other):
        if type(other) == int:
            return self.salary_from == other
        else:
            return self.salary_from == other.salary_from

    def __ne__(self, other):
        if type(other) == int:
            return self.salary_from != other
        else:
            return self.salary_from != other.salary_from

    def __gt__(self, other):
        if type(other) == int:
            return self.salary_from > other
        else:
            return self.salary_from > other.salary_from

    def __ge__(self, other):
        if type(other) == int:
            return self.salary_from >= other
        else:
            return self.salary_from >= other.salary_from

    @staticmethod
    def check_data_int(value):
        """
        Валидатор для целочисленных значений
        """
        if value:
            return value
        return 0

    @staticmethod
    def check_data_str(value):
        """
        Валидатор для стороковых значений
        """
        if value:
            return value
        return "Информация не была найдена"

    @staticmethod
    def filter_vacancies(vacancies_list, filter_words):
        filter_list = []
        for vacancy in vacancies_list:
            for word in filter_words:
                if word in vacancy.description:
                    filter_list.append(vacancy)
                    break
        return filter_list

    @staticmethod
    def get_vacancies_by_salary(filtered_vacancies, min_salary):
        filter_list = []
        for vacancy in filtered_vacancies:
            if vacancy > min_salary:
                filter_list.append(vacancy)
        return filter_list

    @staticmethod
    def sort_vacancies(ranged_vacancies_by_salary):
        return sorted(ranged_vacancies_by_salary, reverse=True)

    @staticmethod
    def get_top_vacancies(sorted_vacancies, top_n):
        return sorted_vacancies[:top_n]
