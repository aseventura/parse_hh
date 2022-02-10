def predict_salary(salary_from, salary_to) -> int:
    if salary_from and salary_to:
        salary = (salary_from + salary_to) / 2
        return int(salary)
    elif salary_from:
        salary = (salary_from * 1.2)
        return int(salary)
    else:
        salary = (salary_to * 0.8)
        return int(salary)