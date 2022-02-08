import os
import requests
from dotenv import load_dotenv
from draw_table import draw_table
from hh import parse_hh_vacancies
from superjob import parse_superjob_vacancies


def main():
    load_dotenv()
    superjob_secret_key = os.getenv('SUPERJOB_SECRET_KEY')
    programming_languages = ('Python', 'Java', 'C++', 'PHP', 'JavaScript', 'Golang', 'Swift', 'Ruby')

    try:
        draw_table(' SuperJob Moscow ', parse_superjob_vacancies(programming_languages, superjob_secret_key))
        draw_table(' HeadHunter Moscow ', parse_hh_vacancies(programming_languages))
    except requests.exceptions.HTTPError:
        print('При соединении с сервером что-то пошло не так..')


if __name__ == '__main__':
    main()