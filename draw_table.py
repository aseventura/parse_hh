from terminaltables import DoubleTable


def prepare_table(statistic_of_languages: dict) -> list:
    basic_table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    for language_name, statistics in statistic_of_languages.items():
        data = [language_name]
        for values in statistics.values():
            data.append(values)
        basic_table_data.append(data)
    return basic_table_data


def draw_table(title: str, statistic_of_languages: dict):
    table_instance = DoubleTable(prepare_table(statistic_of_languages), title)
    print(table_instance.table)
    print()