import requests

from src.abstract_get_api import GetCompaniesAPI


class HeadHunterAPI(GetCompaniesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        """ Конструктор класса """

        self.__url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "per_page": 10, "only_with_vacancies": True}

    def load_user_choice(self, keyword: str):
        """ Метод выгружает данные по запрпосу пользователя """

        self.params["text"] = keyword
        get_response = requests.get(self.__url, headers=self.headers, params=self.params)
        if get_response.status_code != 200:
            raise Exception(f"Ошибка: {get_response.status_code}")
        return get_response.json()["items"]

    def load_data(self):
        """ Метод выгружает данные """
        pass
