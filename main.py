from config import config
from src.utils import create_database, user_choice_employer


def main():
    """ Запуск программы """

    params = config()

    create_database("hh", params)
    user_choice_employer("hh", params)


if __name__ == '__main__':
    main()
