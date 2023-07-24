from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime, date


if __name__ == '__main__':
    current_date = date.today()
    print(current_date)
    name = get_employees('Jon')
    print(name)
    salary = calculate_salary(10_000, 50, '/')
    print(salary)