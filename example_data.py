# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

cities = [
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

schools = [
    {'name': 'Codecool Budapest',
     'city': 'Budapest'},
    {'name': 'Codecool Miskolc',
     'city': 'Miskolc'},
    {'name': 'Codecool Krakow',
     'city': 'Krakow'},
    {'name': 'Codecool Madrid',
     'city': 'Madrid'}
]

mentors = [
        {'first_name': 'Miklós',
         'last_name': 'Beöthy',
         'school_id': 1},
        {'first_name': 'Dániel',
         'last_name': 'Salamon',
         'school_id': 1},
        {'first_name': 'Tamás',
          'last_name': 'Tompa',
          'school_id': 1},
        {'first_name': 'Stanislaw',
          'last_name': 'Bullshitowski',
          'school_id': 3},
        {'first_name': 'Anna',
          'last_name': 'Conda',
          'school_id': 4},
        {'first_name': 'Tibor',
         'last_name': 'Balogh',
         'school_id': 2},
        {'first_name': 'Ethel',
         'last_name': 'Orlando',
         'school_id': 4},
        {'first_name': 'Grandmaster',
         'last_name': 'Algalwillow',
         'school_id': 3},
        {'first_name': 'Pumpkin',
         'last_name': 'Marshmallow',
         'school_id': 2}
]

applicants = [
    {'applicant_code': 'ze23jh',
     'first_name': 'Bob',
     'last_name': 'Marley',
     'year_of_birth': 1966,
     'gender': 'male',
     'city': 'Budapest'}
]


def add_city():
    for city in cities:
        City.create(name=city['city'],
                    nearest_city=city['nearest_city'])


def add_schools():
    for school in schools:
        School.create(name=school['name'],
                      city=school['city'])


def add_mentors():
    for mentor in mentors:
        Mentor.create(first_name=mentor['first_name'],
                      last_name=mentor['last_name'],
                      school_id=mentor['school_id'])

def add_apllicants():
    for applicant in applicants:
        Applicant.create(applicant_code=applicant['applicant_code'],
                         first_name=applicant['first_name'],
                         last_name=applicant['last_name'],
                         year_of_birth=applicant['year_of_birth'],
                         gender=applicant['gender'],
                         city=applicant['city']
                         )

add_city()
add_schools()
add_mentors()
# add_apllicants()
