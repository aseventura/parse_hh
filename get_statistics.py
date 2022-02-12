def get_statistics(agregator, programming_languages: tuple, agregators_secret_key: str=None) -> dict:
    statistic_of_languages = {}
    for language in programming_languages:
        statistic_of_languages[language] = agregator(language, agregators_secret_key)

    return statistic_of_languages