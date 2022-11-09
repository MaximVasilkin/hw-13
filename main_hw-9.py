from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from playsound import playsound

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.datetime.today())
    playsound('Done.mp3')
