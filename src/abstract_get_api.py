from abc import ABC, abstractmethod


class GetCompaniesAPI(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def load_user_choice(self, keyword):
        pass

    def load_data(self):
        pass
