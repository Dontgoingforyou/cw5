from config import config
from src.utils import create_database, user_request, get_and_save_company_data, get_and_save_vacancy_data


def main():
    """ Запуск программы """

    print("Началось получение и сохранение данных...")

    params = config()

    create_database("hh", params)
    get_and_save_company_data("hh", params)
    get_and_save_vacancy_data("hh", params)
    user_request()

    while True:
        user_choice = input("Хотите сделать еще один запрос?\n").lower()
        if user_choice == "да":
            user_request()
        else:
            break


if __name__ == '__main__':
    main()
