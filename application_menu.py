from models import *
from collections import OrderedDict
import datetime
import os
import sys


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
    choice = None

    while choice != '0':
        # clear()
        print("Enter '0' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Menu number: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()


def get_applicant_data():
    """My application data"""
    app_code = input("Please, give your application code: ")
    for applicant in Applicant.select().where(Applicant.application_code == app_code):
        print("Name: {}\nYear of birth: {}\nGender: {}\nSchool: {}\nStatus: {}\n".format(applicant,
              applicant.year_of_birth, applicant.gender, applicant.assigned_school, applicant.status))




menu=OrderedDict([
    ('1', get_applicant_data),
])

menu_loop()
