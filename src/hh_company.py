import requests

from src.abstract_get_api import GetCompaniesAPI


class HeadHunterCompany(GetCompaniesAPI):
    """ Класс для подключения к API работодателя """

    def __init__(self, employer_id):
        self.id_employer = employer_id
        self.__url = f"https://api.hh.ru/employers/{self.id_employer}"  # todo сделать приватным во всех классах
        self.headers = {"User-Agent": "HH-User-Agent"}

    def load_user_choice(self, keyword):
        pass

    def load_data(self):
        get_response = requests.get(self.__url, headers=self.headers)
        data = get_response.json()
        return data
