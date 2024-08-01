from abc import ABC, abstractmethod


class GetCompaniesAPI(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def load_data(self, keyword):
        pass

