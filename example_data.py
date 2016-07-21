# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

cities = [
    {'city': 'Budapest',
     'nearest_school': 'Codecool Budapest'},
    {'city': 'Miskolc',
     'nearest_school': 'Codecool Miskolc'},
    {'city': 'Krakow',
     'nearest_school': 'Codecool Krakow'},
    {'city': 'Madrid',
     'nearest_school': 'Codecool Madrid'},
    {'city': 'Eger',
     'nearest_school': 'Codecool Miskolc'},
    {'city': 'Debrecen',
     'nearest_school': 'Codecool Miskolc'},
    {'city': 'Warsaw',
     'nearest_school': 'Codecool Krakow'},
    {'city': 'Barcelona',
     'nearest_school': 'Codecool Madrid'},
    {'city': 'Győr',
     'nearest_school': 'Codecool Budapest'},
    {'city': 'Paris',
     'nearest_school': 'Codecool Madrid'},
    {'city': 'Rome',
     'nearest_school': 'Codecool Budapest'},
    {'city': 'St. Petersburg',
     'nearest_school': 'Codecool Krakow'}
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

# Can be new/in progress/accepted/rejected
applicants = [
    {'application_code': 'ze23jh',
     'first_name': 'Bob',
     'last_name': 'Marley',
     'year_of_birth': 1966,
     'gender': 'male',
     'city': 'Budapest',
     'status': 'accepted'},

    {'application_code': 'dev666',
     'first_name': 'Devil',
     'last_name': 'Lawyer',
     'year_of_birth': 1966,
     'gender': 'male',
     'city': 'Hell',
     'status': 'rejected'},

    {'application_code': 'nir333',
     'first_name': 'Curt',
     'last_name': 'Cobain',
     'year_of_birth': 1967,
     'gender': 'male',
     'city': 'Rome',
     'status': 'in progress'},

    {'application_code': None,
     'first_name': 'Pam',
     'last_name': 'Pam',
     'year_of_birth': 1993,
     'gender': 'notsure',
     'city': 'Győr',
     'status': 'new'},

    {'application_code': None,
     'first_name': 'Frodo',
     'last_name': 'Baggins',
     'year_of_birth': 2000,
     'gender': 'male',
     'city': 'Debrecen',
     'status': 'new'},

    {'application_code': None,
     'first_name': 'Elvis',
     'last_name': 'Presley',
     'year_of_birth': 1935,
     'gender': 'male',
     'city': 'Barcelona',
     'status': 'new'},

    {'application_code': None,
     'first_name': 'Andreste',
     'last_name': 'Éimhear',
     'year_of_birth': 1909,
     'gender': 'female',
     'city': 'Budapest',
     'status': 'new'},

    {'application_code': None,
     'first_name': 'Jean',
     'last_name': 'D\'Arc',
     'year_of_birth': 1412,
     'gender': 'female',
     'city': 'Paris',
     'status': 'new'},

    {'application_code': None,
     'first_name': 'Krystyna',
     'last_name': 'Rudaski',
     'year_of_birth': 1980,
     'gender': 'female',
     'city': 'Krakkow',
     'status': 'new'}
]


def add_city():
    for city in cities:
        City.create(name=city['city'],
                    nearest_school=city['nearest_school'])


def add_schools():
    for school in schools:
        School.create(name=school['name'],
                      city=school['city'])


def add_mentors():
    for mentor in mentors:
        Mentor.create(first_name=mentor['first_name'],
                      last_name=mentor['last_name'],
                      school_id=mentor['school_id'])


def add_applicants():
    for applicant in applicants:
        Applicant.create(application_code=applicant['application_code'],
                         first_name=applicant['first_name'],
                         last_name=applicant['last_name'],
                         year_of_birth=applicant['year_of_birth'],
                         gender=applicant['gender'],
                         city=applicant['city'],
                         status=applicant['status']
                         )

add_city()
add_schools()
add_mentors()
add_applicants()
