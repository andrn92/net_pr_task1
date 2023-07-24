from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(get_employees('Alex'))
    print(calculate_salary(100_000, 10, '*'))