import requests

from src.abstract_get_api import GetCompaniesAPI


class HeadHunterCompany(GetCompaniesAPI):
    """ Класс для подключения к API работодателя """

    def __init__(self, employer_id: int):
        """ Конструктор класса """

        self.__url = f"https://api.hh.ru/employers/{employer_id}"
        self.headers = {"User-Agent": "HH-User-Agent"}

    def load_data(self):
        """ Метод выгружает данные """

        get_response = requests.get(self.__url, headers=self.headers)
        data = get_response.json()
        return data
