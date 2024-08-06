from src.company import Company
from src.employer import Employer
from src.hh_api import HeadHunterAPI
from src.hh_company import HeadHunterCompany
from src.hh_vacancy import HeadHunterVacancy
from src.vacancy import Vacancy


def user_choice_employer():
    """ Функция для работы с пользователем """

    keyword = input("Введите интересующую вас профессию\n").lower()

    hh_api = HeadHunterAPI()
    employers = hh_api.load_data(keyword)
    employers = [Employer.from_employer_cls(employer) for employer in employers]

    print("Вывод информации о работодателе: \n")
    for employer in employers:
        print(employer)

    if employers:
        employer_id = employers[0].employer_id
        hh_comp = HeadHunterCompany(employer_id)
        companies = hh_comp.load_data(keyword)
        companies = [Company.from_company_cls(company) for company in companies]

        print("Вывод информации о компании: \n")
        for company in companies:
            print(company)

        hh_vac = HeadHunterVacancy(employer_id)
        vacancies = hh_vac.load_data(keyword)
        vacancies = [Vacancy.from_hh_cls(vacancy) for vacancy in vacancies]

        print("Вывод информации о вакансиях компании: \n")
        for vacancy in vacancies:
            print(vacancy)

    else:
        print("Работодатели не найдены.")


user_choice_employer()
