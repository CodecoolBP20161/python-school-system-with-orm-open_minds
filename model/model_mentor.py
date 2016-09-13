from model.model_base import *
from model.model_school import School
from example_data import mentors


class Mentor(BaseModel):
    """  Mentor table based on Mentor model. """
    first_name = CharField()
    last_name = CharField()
    school_id = ForeignKeyField(School, related_name="school_id")
    mentors = mentors

    @staticmethod
    def add_mentors():
        for mentor in Mentor.mentors:
            Mentor.create(first_name=mentor['first_name'],
                          last_name=mentor['last_name'],
                          school_id=School.select().where(School.id==mentor['school_id']))
