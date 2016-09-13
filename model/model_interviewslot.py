from peewee import *
from model.model_mentor import Mentor
from model.model_base import BaseModel
from example_data import interviews


class InterviewSlot(BaseModel):
    """  InterviewSlot table based on InterviewSlot model. """
    date_time = DateTimeField()
    duration = IntegerField()
    mentor = ForeignKeyField(Mentor, related_name='interviews')
    free = BooleanField(default=True)
    # Import from example_data
    interviews = interviews

    def __str__(self):
        return "\nDate and time of the interview: {}\nSchool: {}\nMentor: {} {}\n".format(
            self.date_time, self.duration, self.mentor.first_name, self.mentor.last_name)

    def add_interview_slot():
        for interview in InterviewSlot.interviews:
            InterviewSlot.create(date_time=interview['date_time'],
                                 duration=interview['duration'],
                                 mentor=Mentor.select().where(Mentor.last_name == interview['mentor']),
                                 free=interview['free'])
