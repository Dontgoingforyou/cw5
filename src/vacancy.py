
class Vacancy:
    """ Класс для работы с вакансиями """

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        """ Конструктор класса """

        self.name: str = name
        self.alternate_url: str = alternate_url
        self.salary_from: int = salary_from or 0
        self.salary_to: int = salary_to or 0
        self.area_name: str = area_name
        self.requirement: str = requirement
        self.responsibility: str = responsibility

    def __str__(self) -> str:
        """ Строковое представление вакансии """

        return (f"Наименование вакансии: {self.name}\n"
                f"Ссылка на вакансию: {self.alternate_url}\n"
                f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
                f"Место работы: {self.area_name}\n"
                f"Краткое описание: {self.requirement}\n"
                f"{self.responsibility}\n")

    @classmethod
    def from_hh_cls(cls, vacancy_data: dict):
        """ Метод возвращает экземпляр класса в виде списка """

        salary = vacancy_data.get("salary", {})

        return cls(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            vacancy_data["area"]["name"],
            vacancy_data["snippet"].get("requirement", "Нет данных о требованиях"),
            vacancy_data["snippet"].get("responsibility", "Нет данных об обязанностях"),
        )
