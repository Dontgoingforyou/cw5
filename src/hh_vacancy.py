import requests

from src.abstract_get_api import GetCompaniesAPI


class HeadHunterVacancy(GetCompaniesAPI):
    """ Класс для подключения к API вакансии работодателя """

    def __init__(self, vacancies_id):
        """ Конструктор класса """

        self.__url = f"https://api.hh.ru/vacancies?employer_id={vacancies_id}"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"per_page": 100}

    def load_data(self):
        """ Метод выгружает данные """

        get_response = requests.get(self.__url, headers=self.headers, params=self.params)
        data = get_response.json()['items']

        return data
