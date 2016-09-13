from model_base import *
from model_school import School


class City(BaseModel):
    """  City table based on City model. """
    name = CharField()
    nearest_school = ForeignKeyField(School, related_name='nearest_school', null=True)

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

    @staticmethod
    def add_cities():
        for city in City.cities:
            City.create(name=city['city'], nearest_school=School.select().where(School.name==city['nearest_school']))
