from datetime import datetime

from application.db.people import get_employees
from application.salary import calculate_salary


def get_date():
    print(f'Дата:{datetime.date(datetime.now())}')


if __name__ == '__main__':
    get_date()
    calculate_salary()
    get_employees()
