from application.db.people import get_employees
from application.salary import calculate_salary
import datetime


class Employee:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    employee = Employee("Vasya")
    print(employee.name)
    calculate_salary()
    get_employees()
    date_today = datetime.date.today()
    print(date_today)
