class Employer:
    """ Класс для работы с работодателем """

    __slots__ = ("employer_id", "name", "url", "alternate_url", "vacancies_url")

    def __init__(self, employer_id, name, url, alternate_url, vacancies_url):
        """ Конструктор класса """

        self.employer_id: str = employer_id
        self.name: str = name
        self.url: str = url
        self.alternate_url: str = alternate_url
        self.vacancies_url: str = vacancies_url

    def __str__(self) -> str:
        """ Строковое представление данных о работодателе """

        return (f"ID компании: {self.employer_id}\n"
                f"Название компаний: {self.name}\n"
                f"Ссылка на API вакансии: {self.url}\n"
                f"Ссылка на вакансии на hh.ru: {self.alternate_url}\n"
                f"Ссылка на открытые вакансии компаний: {self.vacancies_url}\n")

    @classmethod
    def from_employer_cls(cls, employer_data):
        """ Метод возвращает экземпляр класса """

        return cls(
            employer_data["id"],
            employer_data["name"],
            employer_data["url"],
            employer_data["alternate_url"],
            employer_data["vacancies_url"],
        )


# emp = Employer("UNION SPACE GROUP (HAYFIL CONSALTING)", "https://api.hh.ru/employers/1862997",
#                "https://hh.ru/employer/1862997", "https://api.hh.ru/vacancies?employer_id=1862997")
#
# print(emp)
