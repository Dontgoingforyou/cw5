from config import config
from src.utils import create_database, user_choice_employer, user_request


def main():
    """ Запуск программы """

    params = config()

    create_database("hh", params)
    user_choice_employer("hh", params)
    user_request()

    while True:
        user_choice = input("Хотите сделать еще один запрос?\n").lower()
        if user_choice == "да":
            user_request()
        else:
            break


if __name__ == '__main__':
    main()
