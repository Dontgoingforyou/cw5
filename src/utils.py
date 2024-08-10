import psycopg2

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
    employers_data = hh_api.load_user_choice(keyword)
    employers = [Employer.from_employer_cls(employer) for employer in employers_data]

    print("Вывод информации о работодателе: \n")
    for employer in employers:
        print(employer)

    companies_data = [HeadHunterCompany(employer['employer']['id']).load_data() for employer in employers_data]
    print(type(companies_data))
    companies = [Company.from_company_cls(company) for company in companies_data]
    for company in companies:
        print(company)

    vacancy_data = [HeadHunterVacancy(employer['employer']['id']).load_data() for employer in employers_data]
    print(type(vacancy_data))
    vacancies = [Vacancy.from_vacancy_cls(vacancy) for vacancy in vacancy_data]
    print(f"DEBUG {vacancies}")
    for vacancy in vacancies:
        print(vacancy)


user_choice_employer()

# def create_database(database_name: str, params: dict) -> None:
#     """ Создание БД и таблиц для сохранения данных о компаниях и вакансиях """
#
#     conn = psycopg2.connect(dbname=database_name, **params)
#     conn.autocommit = True
#     cur = conn.cursor()
#
#     cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
#     cur.execute(f"CREATE DATABASE {database_name}")
#
#     cur.close()
#     conn.close()
#
#     conn = psycopg2.connect(dbname=database_name, **params)
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#
#             """
#         )
