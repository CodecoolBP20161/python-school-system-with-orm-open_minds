# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

Cities = [
    {'city': 'Budapest'}
    {'city': 'Miskolc'}
    {'city': 'Krakow'}
    {'city': 'Madrid'}
]

Schools = [
    {'name': 'Codecool Budapest'
     'city': 'Budapest'}
    {'name': 'Codecool Miskolc'
     'city': 'Miskolc'}
]


def add_city():
    for city in Cities:
        City.create(name=city['city'])


def add_schools():
    for school in Schools:
        Schools.create(name=['name']
                       city=['city'])
