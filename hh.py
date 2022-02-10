import requests
from predict_salary import predict_salary


def predict_rub_salary_for_hh(vacancy_info: dict):
    if vacancy_info['salary'] and vacancy_info['salary']['currency'] == 'RUR':
        return predict_salary(vacancy_info['salary']['from'], vacancy_info['salary']['to'])


def parse_hh_vacancies(programming_languages: tuple) -> dict:
    base_url = 'https://api.hh.ru/vacancies'
    statistic_of_languages = {}

    for language in programming_languages:
        language_info = {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
        }
        query_string = {
            'area': '1',                    # Moscow location
            'period': '30',                 # Last 30 days
            'text': language,               # Search field
            'page': 0,                      # Start page
        }
        hh_pages = 1
        all_vacancies = []
        while query_string['page'] < hh_pages:
            response = requests.get(base_url, params=query_string)
            response.raise_for_status()
            hh_response = response.json()
            language_info['vacancies_found'] = hh_response['found']
            all_vacancies += hh_response['items']
            hh_pages = hh_response['pages']
            query_string['page'] += 1

        for vacancy in all_vacancies:
            job_salary = predict_rub_salary_for_hh(vacancy)
            if job_salary:
                language_info['vacancies_processed'] += 1
                language_info['average_salary'] += job_salary
        language_info['average_salary'] = int(language_info['average_salary'] / language_info['vacancies_processed'])
        statistic_of_languages[language] = language_info

    return statistic_of_languages