import requests
from predict_salary import predict_salary


def predict_rub_salary_for_hh(vacancy_info: dict):
    if vacancy_info['salary'] and vacancy_info['salary']['currency'] == 'RUR':
        return predict_salary(vacancy_info['salary']['from'], vacancy_info['salary']['to'])
    return


def parse_hh_vacancies(programming_languages: tuple) -> dict:
    base_url = 'https://api.hh.ru/vacancies'
    search_requests = (
        'Python Django NOT go NOT golang', 'Java Spring', 'C++ Boost', 'PHP Symphony',
        'JavaScript React NOT Angular', 'Golang NOT python', 'Swift iOS', 'Ruby Rails',
    )
    statistic_of_languages = {}

    for i, language in enumerate(programming_languages):
        language_info = {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
        }
        query_string = {
            'area': '1',                    # Moscow location
            'period': '30',                 # Last 30 days
            'text': search_requests[i],     # Search field
            'page': 0,                      # Start page
        }
        response = requests.get(base_url, params=query_string)
        response.raise_for_status()
        language_info['vacancies_found'] = response.json()['found']
        search_results = response.json()['items']

        while query_string['page'] < response.json()['pages']:
            query_string['page'] += 1
            response = requests.get(base_url, params=query_string)
            response.raise_for_status()
            search_results += response.json()['items']

        for vacancy_info in search_results:
            job_salary = predict_rub_salary_for_hh(vacancy_info)
            if job_salary:
                language_info['vacancies_processed'] += 1
                language_info['average_salary'] += job_salary
        language_info['average_salary'] = int(language_info['average_salary'] / language_info['vacancies_processed'])
        statistic_of_languages[language] = language_info

    return statistic_of_languages