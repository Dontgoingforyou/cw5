import requests

from src.abstract_get_api import GetCompaniesAPI
from src.employer import Employer


class HeadHunterCompany(GetCompaniesAPI):
    """ Класс для подключения к API работодателя """

    def __init__(self):
        self.id_employer = Employer.employer_id
        self.url = f"https://api.hh.ru/employers/{self.id_employer}"
        self.headers = {"User-Agent": "HH-User-Agent"}

    def load_data(self, keyword):
        get_response = requests.get(self.url, headers=self.headers)
        return get_response.json()
