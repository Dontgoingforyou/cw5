class Company:
    """ Класс для работы с компанией """

    __slots__ = ("description", "site_url", "industries_name", "open_vacancies")

    def __init__(self, description, site_url, industries_name, open_vacancies):
        """ Конструктор класса """

        self.description: str = description
        self.site_url: str = site_url
        self.industries_name: str = industries_name
        self.open_vacancies: int = open_vacancies

    def __str__(self):
        """ Строковое представление данных о компании """

        return (f"Описание компании: {self.description}\n"
                f"URL-адрес компании: {self.site_url}\n"
                f"Отрасль: {self.industries_name}\n"
                f"Количество открытых вакансии: {self.open_vacancies}")

    @classmethod
    def from_company_cls(cls, company_data):
        """ Метод возвращает экземпляр класса """

        if isinstance(company_data, dict):
            return cls(
                company_data["description"],
                company_data["site_url"],
                company_data["industries"]["name"],
                company_data["open_vacancies"],
            )
        else:
            print("Ошибка: данные компании должны быть словарем")
            return None

