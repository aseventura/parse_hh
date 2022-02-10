import requests
from predict_salary import predict_salary


def fetch_rub_salary_for_superJob(vacancy: dict) -> int:
    if vacancy['currency'] == 'rub':
        return predict_salary(vacancy['payment_from'], vacancy['payment_to'])
    return


def parse_superjob_vacancies(programming_languages: tuple, superjob_secret_key: str) -> dict:
    base_url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': superjob_secret_key,
    }
    statistic_of_languages = {}

    for language in programming_languages:
        language_info = {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
        }
        query_string = {
            'keyword': language,                    # Search Field
            'town': '4',                            # Moscow Location
            'catalogues': '48',                     # Разработка, программирование
            'page': 0,
        }
        superjob_pages = True
        all_vacancies = []

        while superjob_pages:
            response = requests.get(base_url, headers=headers, params=query_string)
            response.raise_for_status()
            superjob_response = response.json()
            language_info['vacancies_found'] = superjob_response['total']
            all_vacancies += superjob_response['objects']
            superjob_pages = superjob_response['more']
            query_string['page'] += 1

        for vacancy in all_vacancies:
            job_salary = fetch_rub_salary_for_superJob(vacancy)
            if job_salary:
                language_info['vacancies_processed'] += 1
                language_info['average_salary'] += job_salary
        language_info['average_salary'] = int(language_info['average_salary'] / language_info['vacancies_processed'])
        statistic_of_languages[language] = language_info

    return statistic_of_languages