import psycopg2
import itertools

from src.company import Company
from src.employer import Employer
from src.hh_api import HeadHunterAPI
from src.hh_company import HeadHunterCompany
from src.hh_vacancy import HeadHunterVacancy
from src.vacancy import Vacancy


def user_choice_employer(database_name: str, params: dict) -> None:
    """ Функция для работы с пользователем """

    keyword = input("Введите интересующую вас профессию\n").lower()

    hh_api = HeadHunterAPI()
    employers_data = hh_api.load_user_choice(keyword)
    employers = [Employer.from_employer_cls(employer) for employer in employers_data]

    companies_data = [HeadHunterCompany(employer['employer']['id']).load_data() for employer in employers_data]
    companies = [Company.from_company_cls(company) for company in companies_data]

    vacancy_data = list(itertools.chain.from_iterable(
        [HeadHunterVacancy(employer['employer']['id']).load_data() for employer in employers_data]))
    vacancies = [Vacancy.from_vacancy_cls(vacancy) for vacancy in vacancy_data]

    for employer in employers:
        employers_data = {
            "employer_id": employer.employer_id,
            "employer_name": employer.name,
            "employer_url": employer.url,
            "alternate_url": employer.alternate_url,
            "employer_vacancies_url": employer.vacancies_url
        }
        save_data_to_database('employers', employers_data, database_name, params)

    for company in companies:
        companies_data = {
            "company_description": company.description,
            "company_site_url": company.site_url,
            "open_vacancies": company.open_vacancies
        }
        save_data_to_database('companies', companies_data, database_name, params)

    for vacancy in vacancies:
        vacancy_data = {
            "vacancy_name": vacancy.name,
            "alternate_url": vacancy.alternate_url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "salary_currency": vacancy.salary_currency,
            "vacancy_area_name": vacancy.area_name,
            "requirement": vacancy.requirement,
            "responsibility": vacancy.responsibility
        }
        save_data_to_database('vacancies', vacancy_data, database_name, params)

    print(f"Вся информация сохранена в базу данных {database_name}")


def create_database(database_name: str, params: dict) -> None:
    """ Создание БД и таблиц для сохранения данных о компаниях и вакансиях """

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE employers (
                employer_id INTEGER,
                employer_name TEXT NOT NULL,
                employer_url TEXT,
                alternate_url TEXT UNIQUE,
                employer_vacancies_url TEXT
            )
        """)

    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE companies (
                company_description TEXT,
                company_site_url TEXT,
                open_vacancies INTEGER
            )
        """)

    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE vacancies (
                vacancy_name VARCHAR,
                alternate_url TEXT,
                salary_from INTEGER,
                salary_to INTEGER,
                salary_currency VARCHAR,
                vacancy_area_name VARCHAR,
                requirement TEXT,
                responsibility TEXT
            )
        """)

    conn.commit()
    conn.close()


def save_data_to_database(table_name: str, data: dict, database_name: str, params: dict) -> None:

    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True
    cur = conn.cursor()

    columns = ', '.join(data.keys())
    values = ', '.join(["%s"] * len(data))

    sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

    cur.execute(sql_query, list(data.values()))

    cur.close()
    conn.close()
