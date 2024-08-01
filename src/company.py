class Company:
    """ Класс для работы с компанией """

    __slots__ = ("description", "site_url", "industries_name")

    def __init__(self, description, site_url, industries_name):
        """ Конструктор класса """

        self.description = description
        self.site_url = site_url
        self.industries_name = industries_name

    def __str__(self):
        """ Строковое представление данных о компании """

        return (f"Описание компании: {self.description}\n"
                f"URL-адрес компании: {self.site_url}\n"
                f"Отрасль: {self.industries_name}\n")

    @classmethod
    def from_company_cls(cls, company_data):
        """ Метод возвращает экземпляр класса """

        return cls(
            company_data["description"],
            company_data["site_url"],
            company_data["industries"]["name"]
        )
    