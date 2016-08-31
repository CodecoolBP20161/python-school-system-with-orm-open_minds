from peewee import *
from server import app
from flask_peewee.db import Database

db = Database(app)


class Applicant(db.Model):
    """  Applicant table based on Applicant model. """
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    year_of_birth = IntegerField()
    gender = CharField()
    city = CharField()
    assigned_school = ForeignKeyField(School, related_name='applicants', null=True)
    interview_slot = ForeignKeyField(InterviewSlot, related_name='applicants', null=True)
    status = CharField()
