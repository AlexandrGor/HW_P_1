import datetime as dt
from application.salary import calculate_salary
from application.db.people import get_employees

def now():
    return str(dt.date.today())

if __name__ == '__main__':
    print(get_employees(), now())
    print(calculate_salary(), now())