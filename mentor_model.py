from models import *


class Mentor(BaseModel):
    """  Mentor table based on Mentor model. """
    first_name = CharField()
    last_name = CharField()
    # school_id = ForeignKeyField()
    school_id = IntegerField()
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

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return "Name: {}\nApplicant code: {}\nYear of birth: {}\nGender: {}\nCity: {}\nSchool: {}\nStatus: {}\n".format\
            (full_name, self.application_code, self.year_of_birth,
             self.gender, self.city, self.assigned_school, self.status)

    @staticmethod
    def add_mentors():
        for mentor in Mentor.mentors:
            Mentor.create(first_name=mentor['first_name'],
                          last_name=mentor['last_name'],
                          school_id=mentor['school_id'])
