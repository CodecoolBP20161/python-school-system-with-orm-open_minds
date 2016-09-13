from model.model_base import *
from model.model_school import School


class Mentor(BaseModel):
    """  Mentor table based on Mentor model. """
    first_name = CharField()
    last_name = CharField()
    school_id = ForeignKeyField(School, related_name="school_id")
    mentors = [
        {'first_name': 'Miklos',
         'last_name': 'Beothy',
         'school_id': 1},
        {'first_name': 'Daniel',
         'last_name': 'Salamon',
         'school_id': 1},
        {'first_name': 'Tamas',
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

    @staticmethod
    def add_mentors():
        for mentor in Mentor.mentors:
            Mentor.create(first_name=mentor['first_name'],
                          last_name=mentor['last_name'],
                          school_id=School.select().where(School.id==mentor['school_id']))
