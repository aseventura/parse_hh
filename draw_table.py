from terminaltables import DoubleTable


def prepare_table(statistic_of_languages: dict) -> list:
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    for language, statistics in statistic_of_languages.items():
        temp_data = [language]
        for value in statistics.values():
            temp_data.append(value)
        table_data.append(temp_data)
    return table_data


def draw_table(title: str, statistic_of_languages: dict):
    table_instance = DoubleTable(prepare_table(statistic_of_languages), title)
    print(table_instance.table)
    print()