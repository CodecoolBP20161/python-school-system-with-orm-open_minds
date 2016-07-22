from collections import OrderedDict
from models import *
import os

# This clears the terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# This is the main loop, which handling the sub menu choices.
def applicant_menu_loop():
    """Applicant"""
    choice = None

    while choice != '0':
        # clear()
        print("Enter '0' to main menu.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Menu number: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

"""
This section defines the sub menu choices.
"""


def get_applicant_data():
    """My application data"""
    app_code = input("Please, give your application code: ")
    for applicant in Applicant.select().where(Applicant.application_code == app_code):
        print(applicant)


def get_interview_details():
    """My personal interview data"""
    app_code = input("Please, give your application code: ")
    for interview in InterviewSlot.select().where(InterviewSlot.applicant == app_code):
        print("\nSchool: {}\nDate and time of interview: {}\nMentor: {}\n".format(
              interview.school_name, interview.date_time, interview.mentor))

# This library allows you can choose an operation.
menu=OrderedDict([
    ('1', get_applicant_data),
    ('2', get_interview_details)
])
