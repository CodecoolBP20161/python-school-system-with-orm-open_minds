from models import *


class School(BaseModel):
    """  School table based on School model. """
    name = CharField()

    schools = [
        {'name': 'Codecool Budapest'},
        {'name': 'Codecool Miskolc'},
        {'name': 'Codecool Krakow'},
        {'name': 'Codecool Madrid'}
    ]

    @staticmethod
    def add_schools():
        for school in School.schools:
            School.create(name=school['name'])
