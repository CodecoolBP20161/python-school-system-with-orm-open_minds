from peewee import *
from models import BaseModel
from mentor_model import Mentor


class InterviewSlot(BaseModel):
    """  InterviewSlot table based on InterviewSlot model. """
    date_time = DateTimeField()
    duration = IntegerField()
    mentor = ForeignKeyField(Mentor, related_name='interviews')
    free = BooleanField(default=True)

    interviews = [
        {'date_time': '2016-11-20 10:00:00',
         'duration': 2,
         'mentor': 'Beothy',
         'free': True},
        {'date_time': '2016-11-27 10:00:00',
         'duration': 2,
         'mentor': 'Tompa',
         'free': True},
        {'date_time': '2016-12-24 14:00:00',
         'duration': 2,
         'mentor': 'Salamon',
         'free': True},
        {'date_time': '2016-12-11 14:00:00',
         'duration': 2,
         'mentor': 'Balogh',
         'free': True},
        {'date_time': '2017-1-4 10:00:00',
         'time': '10:00',
         'duration': 2,
         'mentor': 'Bullshitowski',
         'free': True},
        {'date_time': '2017-1-12 15:00:00',
         'duration': 2,
         'mentor': 'Conda',
         'free': True},
        {'date_time': '2017-1-20 14:00:00',
         'duration': 2,
         'mentor': 'Orlando',
         'free': True},
        {'date_time': '2016-10-20 10:00:00',
         'duration': 2,
         'mentor': 'Algalwillow',
         'free': True},
        {'date_time': '2016-11-15 8:00:00',
         'duration': 2,
         'mentor': 'Marshmallow',
         'free': True}
    ]

    def __str__(self):
        return "\nDate and time of the interview: {}\nSchool: {}\nMentor: {} {}\n".format(
            self.date_time, self.duration, self.mentor.first_name, self.mentor.last_name)

    def add_interview_slot():
        for interview in InterviewSlot.interviews:
            InterviewSlot.create(date_time=interview['date_time'],
                                 duration=interview['duration'],
                                 mentor=Mentor.select().where(Mentor.last_name == interview['mentor']),
                                 free=interview['free'])
