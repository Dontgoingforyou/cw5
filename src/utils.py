import progressbar
import psycopg2

from config import config
from src.DBManager import DBManager
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

    bar = progressbar.ProgressBar(maxval=len(employers_data))
    bar.start()
    companies_data = []
    for i, employer in enumerate(employers_data):
        companies_data.append(HeadHunterCompany(employer['employer']['id']).load_data())
        bar.update(i + 1)
    bar.finish()
    companies = [Company.from_company_cls(company) for company in companies_data]

    bar = progressbar.ProgressBar(maxval=len(employers_data))
    bar.start()
    vacancy_data = []
    for i, employer in enumerate(employers_data):
        vacancy_data.extend(HeadHunterVacancy(employer['employer']['id']).load_data())
        bar.update(i + 1)
    bar.finish()
    vacancies = [Vacancy.from_vacancy_cls(vacancy) for vacancy in vacancy_data]

    bar = progressbar.ProgressBar(maxval=len(employers))
    bar.start()
    for i, employer in enumerate(employers):
        employers_data = {
            "employer_id": employer.employer_id,
            "employer_name": employer.name,
            "employer_url": employer.url,
            "alternate_url": employer.alternate_url,
            "employer_vacancies_url": employer.vacancies_url
        }
        save_data_to_database('employers', employers_data, database_name, params)
        bar.update(i + 1)
    bar.finish()

    bar = progressbar.ProgressBar(maxval=len(companies))
    bar.start()
    for i, company in enumerate(companies):
        companies_data = {
            "company_description": company.description,
            "company_site_url": company.site_url,
            "open_vacancies": company.open_vacancies
        }
        save_data_to_database('companies', companies_data, database_name, params)
        bar.update(i + 1)
    bar.finish()

    bar = progressbar.ProgressBar(maxval=len(vacancies))
    bar.start()
    for i, vacancy in enumerate(vacancies):
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
        bar.update(i + 1)
    bar.finish()

    print(f"Вся информация сохранена в базу данных {database_name}\n")


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


def user_request():

    params = config()
    db_manager = DBManager("hh", params)

    user_input = input("Выберите запрос:\n"
                       "1 - Вывести список всех компаний и количество вакансии у каждой компании\n"
                       "2 - Вывести список всех вакансии с указанием названия компании, названия вакансии и зарплаты "
                       "и ссылки на вакансию\n"
                       "3 - Вывести среднюю зарплату по вакансиям\n"
                       "4 - Вывести список всех вакансии, у которых зарплата выше средней по всем вакансиям\n"
                       "5 - Вывести список всех вакансии, в названии которых содержится запрашиваемое слово\n")

    if user_input == "1":
        companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
        print("Список всех компаний и количество вакансии у каждой компании:\n")
        for i in companies_and_vacancies_count:
            print(i)

    elif user_input == "2":
        all_vacancies = db_manager.get_all_vacancies()
        print("Cписок всех вакансии с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию:"
              "\n")
        for i in all_vacancies:
            print(i)

    elif user_input == "3":
        avg_salary = db_manager.get_avg_salary()
        print(f"Средняя зарплата по вакансиям: {avg_salary}\n")
        for i in avg_salary:
            print(i)

    elif user_input == "4":
        vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
        print("Список всех вакансии, у которых зарплата выше средней по всем вакансиям:\n")
        for i in vacancies_with_higher_salary:
            print(i)

    elif user_input == "5":
        user_choice = input("Введите ключевое слово\n")
        vacancies_with_keyword = db_manager.get_vacancies_with_keyword(user_choice)
        print("Список всех вакансии, в названии которых содержится запрашиваемое слово:\n")
        for i in vacancies_with_keyword:
            print(i)
