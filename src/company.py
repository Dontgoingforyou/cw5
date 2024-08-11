from typing import Any


class Company:
    """ Класс для работы с компанией """

    __slots__ = ("description", "site_url", "open_vacancies")

    def __init__(self, description, site_url, open_vacancies):
        """ Конструктор класса """

        self.description: str = description
        self.site_url: str = site_url
        self.open_vacancies: int = open_vacancies

    def __str__(self) -> str:
        """ Строковое представление данных о компании """

        return (f"Описание компании: {self.description}\n"
                f"URL-адрес компании: {self.site_url}\n"
                f"Количество открытых вакансии: {self.open_vacancies}\n")

    @classmethod
    def from_company_cls(cls, company_data: dict) -> Any:
        """ Метод возвращает экземпляр класса """

        if isinstance(company_data, dict):
            return cls(
                company_data.get("description", "Нет описания"),
                company_data.get("site_url", "Нет URL"),
                company_data.get("open_vacancies", 0),
            )
        else:
            print("Ошибка: данные компании должны быть словарем")
            return None

