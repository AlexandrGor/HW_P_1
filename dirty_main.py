import datetime as dt
from application import *

def now():
    return str(dt.date.today())

if __name__ == '__main__':
    print(db.people.get_employees(), now())
    print(salary.calculate_salary(), now())
