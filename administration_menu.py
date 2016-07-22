from collections import OrderedDict
from models import *
import os


# This clears the terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# This is the main loop, which handles the sub menu choices.
def administrator_menu_loop():
    """Administrator"""
    choice = None

    while choice != '0':
        print("Please choose a filter!")
        print("Enter '0' to exit to main menu.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Menu number: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

"""
This section defines the submenu choices.
"""


def filter_by_status():
    """Filter applicants by status"""
    answer = input("Enter a status (new/in progress/accepted/rejected): ")
    for applicant in Applicant.select().where(Applicant.status.contains(answer)):
        print(applicant)


def filter_by_year():
    """Filter applicants by year of birth"""
    answer = input("Enter a year: ")
    for applicant in Applicant.select().where(Applicant.year_of_birth == answer):
        print(applicant)


def filter_by_location():
    """Filter applicants by their location"""
    answer = input("Enter a location: ")
    for applicant in Applicant.select().where(Applicant.city.contains(answer)):
        print(applicant)


def filter_by_name():
    """Filter applicants by name"""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    for applicant in Applicant.select().where((Applicant.first_name.contains(first_name))
                                                      & (Applicant.contains(last_name))):
        print(applicant)


def filter_by_school():
    """Filter applicants by assigned school"""
    answer = input("Enter a school: ")
    for applicant in Applicant.select().where(Applicant.assigned_school.contains(answer)):
        print(applicant)


def filter_by_mentor_name():
    """Filter applicants by assigned mentors"""
    answer = input("Enter mentor's name: ")
    for applicant in Applicant.select().join(InterviewSlot,
                                             on=(Applicant.application_code==InterviewSlot.applicant))\
            .where(InterviewSlot.mentor.contains(answer)):
        print(applicant)


# This library allows you to choose an operation.
menu = OrderedDict([
    ('1', filter_by_status),
    ('2', filter_by_year),
    ('3', filter_by_location),
    ('4', filter_by_name),
    ('5', filter_by_school),
    ('6', filter_by_mentor_name),
])
