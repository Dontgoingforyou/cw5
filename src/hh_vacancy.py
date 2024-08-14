import requests

from src.abstract_get_api import GetCompaniesAPI


class HeadHunterVacancy(GetCompaniesAPI):
    """ Класс для подключения к API вакансии работодателя """

    def __init__(self, employer_id):
        """ Конструктор класса """

        self.id_employer = employer_id
        self.__url = f"https://api.hh.ru/vacancies?employer_id={self.id_employer}"
        self.headers = {"User-Agent": "HH-User-Agent"}

    def load_user_choice(self, keyword):
        """ Метод выгружает данные по запрпосу пользователя """
        pass

    def load_data(self):
        """ Метод выгружает данные """

        get_response = requests.get(self.__url, headers=self.headers)
        data = get_response.json()['items']

        return data
