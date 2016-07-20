# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

Cities = [
    {'city': 'Eger',
     'nearest_city': 'Miskolc'},
    {'city': 'Debrecen',
     'nearest_city': 'Miskolc'},
    {'city': 'Warsaw',
     'nearest_city': 'Krakow'},
    {'city': 'Barcelona',
     'nearest_city': 'Madrid'},
    {'city': 'Győr',
     'nearest_city': 'Budapest'},
    {'city': 'Paris',
     'nearest_city': 'Madrid'},
    {'city': 'Rome',
     'nearest_city': 'Budapest'},
    {'city': 'St. Petersburg',
     'nearest_city': 'Krakow'}
]

Schools = [
    {'name': 'Codecool Budapest',
     'city': 'Budapest'},
    {'name': 'Codecool Miskolc',
     'city': 'Miskolc'},
    {'name': 'Codecool Krakow',
     'city': 'Krakow'},
    {'name': 'Codecool Madrid',
     'city': 'Madrid'}
]


def add_city():
    for city in Cities:
        City.create(name=city['city'],
                    nearest_city=city['nearest_city'])


def add_schools():
    for school in Schools:
        School.create(name=school['name'],
                      city=school['city'])


add_city()
add_schools()
