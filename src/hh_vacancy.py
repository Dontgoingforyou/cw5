import requests

from src.abstract_get_api import GetCompaniesAPI


class HeadHunterVacancy(GetCompaniesAPI):
    """ Класс для подключения к API вакансии работодателя """

    def __init__(self, employer_id):
        self.id_employer = employer_id

    def load_data(self, keyword):
        response = requests.get(f"https://api.hh.ru/vacancies?employer_id={self.id_employer}")
        if response.status_code == 200:
            return response.json().get("items", [])
        return []