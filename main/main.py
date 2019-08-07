from application.salary import calculate_salary
from db.people import get_employees

if __name__ == '__main__':
    get_employees()
    calculate_salary()