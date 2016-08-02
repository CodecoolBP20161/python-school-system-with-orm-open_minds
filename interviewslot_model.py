from peewee import *
from models import BaseModel
from mentor_model import Mentor
from applicant_model import Applicant
from school_model import School


class InterviewSlot(BaseModel):
    """  InterviewSlot table based on InterviewSlot model. """
    date_time = DateTimeField()
    duration = IntegerField()
    mentor = ForeignKeyField(Mentor, related_name='mentor')
    applicant = ForeignKeyField(Applicant, related_name='applicant', null = True)
    school_name = ForeignKeyField(School, related_name='school')

    interviews = [
        {'date_time': '2016-11-20 10:00:00',
         'duration': 2,
         'mentor': 'Beöthy',
         'applicant': 'thc420',
         'school_name': 'Codecool Budapest'},
        {'date_time': '2016-11-27 10:00:00',
         'duration': 2,
         'mentor': 'Tompa',
         'applicant': 'dev666',
         'school_name': 'Codecool Budapest'},
        {'date_time': '2016-12-24 14:00:00',
         'duration': 2,
         'mentor': 'Salamon',
         'applicant': 'nir333',
         'school_name': 'Codecool Budapest'},
        {'date_time': '2016-12-11 14:00:00',
         'duration': 2,
         'mentor': 'Balogh',
         'applicant': None,
         'school_name': 'Codecool Miskolc'},
        {'date_time': '2017-1-4 10:00:00',
         'time': '10:00',
         'duration': 2,
         'mentor': 'Bullshitowski',
         'applicant': None,
         'school_name': 'Codecool Krakow'},
        {'date_time': '2017-1-12 15:00:00',
         'duration': 2,
         'mentor': 'Conda',
         'applicant': None,
         'school_name': 'Codecool Madrid'},
        {'date_time': '2017-1-20 14:00:00',
         'duration': 2,
         'mentor': 'Orlando',
         'applicant': None,
         'school_name': 'Codecool Madrid'},
        {'date_time': '2016-10-20 10:00:00',
         'duration': 2,
         'mentor': 'Algalwillow',
         'applicant': None,
         'school_name': 'Codecool Krakow'},
        {'date_time': '2016-11-15 8:00:00',
         'duration': 2,
         'mentor': 'Marshmallow',
         'applicant': None,
         'school_name': 'Codecool Miskolc'}
    ]

    def add_interview_slot():
        for interview in InterviewSlot.interviews:
            InterviewSlot.create(date_time=interview['date_time'],
                                 duration=interview['duration'],
                                 mentor=Mentor.select().where(Mentor.last_name == interview['mentor']),
                                 applicant=Applicant.select().where(Applicant.application_code==interview['applicant']),
                                 school_name=School.select().where(School.name == interview['school_name']))
