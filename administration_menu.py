from collections import OrderedDict
from models import *
import os


# This clears the terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# This is the main loop, which handling the sub menu choices.
def administrator_menu_loop():
    """Administrator"""
    choice = None

    while choice != '0':
        print("Choose a filter on what you want to order the applicants!")
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


def filter_by_status():
    """Filter by status"""
    answer = input("Give me a kind of status: ")
    for applicant in Applicant.select().where(Applicant.status.contains(answer)):
        print(applicant)


def filter_by_year():
    """Filter by year"""
    answer = input("Give me a year: ")
    for applicant in Applicant.select().where(Applicant.year_of_birth == answer):
        print(applicant)


def filter_by_location():
    """Filter by location"""
    answer = input("Give me a location: ")
    for applicant in Applicant.select().where(Applicant.city.contains(answer)):
        print(applicant)


def filter_by_name():
    """Filter by name"""
    first_name = input("Give me first name: ")
    last_name = input("Give me last name: ")
    for applicant in Applicant.select().where((Applicant.first_name.contains(first_name))
                                                      & (Applicant.contains(last_name))):
        print(applicant)


def filter_by_school():
    """Filter by school"""
    answer = input("Give me a school: ")
    for applicant in Applicant.select().where(Applicant.assigned_school.contains(answer)):
        print(applicant)


def filter_by_mentor_name():
    """Filter by mentor name"""
    answer = input("Give me a mentor name: ")
    for applicant in Applicant.select().join(InterviewSlot,
                                             on=(Applicant.application_code==InterviewSlot.applicant))\
            .where(InterviewSlot.mentor.contains(answer)):
        print(applicant)


# This library allows you can choose an operation.
menu = OrderedDict([
    ('1', filter_by_status),
    ('2', filter_by_year),
    ('3', filter_by_location),
    ('4', filter_by_name),
    ('5', filter_by_school),
    ('6', filter_by_mentor_name),
])
