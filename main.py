import os.path

from src.vacancy import Vacancy
from src.hh import HH
from src.json_worker import JsonWorker
from src.utils import print_vacancies

BASE_DIR = os.path.dirname(__file__)
PATH_TO_DATA_FILE = os.path.join(BASE_DIR, "data", "vacancies.json")

def main():
    hh_api = HH()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.vacancies_list(hh_vacancies)
    top_n = int(input("Введите количество вакансий для вывода по цене в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    min_salary = int(input("Введите минимальную зарплату: ")) # Пример: 100000
    #
    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)
    #
    ranged_vacancies_by_salary = Vacancy.get_vacancies_by_salary(filtered_vacancies, min_salary)
    #
    sorted_vacancies = Vacancy.sort_vacancies(ranged_vacancies_by_salary)
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    json_saver = JsonWorker(PATH_TO_DATA_FILE)
    json_saver.write_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
