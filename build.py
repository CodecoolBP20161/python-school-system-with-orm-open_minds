from basemodel import *
from school_model import School
from city_model import City
from mentor_model import Mentor
from applicant_model import Applicant
from interviewslot_model import InterviewSlot


def build():
    db = PostgresqlDatabase("")
    db.connect()
    db.drop_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)
    db.create_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)
