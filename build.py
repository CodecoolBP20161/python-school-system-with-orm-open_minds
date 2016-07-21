from models import *


def build():

    db.connect()
    # List the tables here what you want to create...
    db.drop_tables([Applicant, Mentor, School, City, InterviewSlot], safe=True)
    db.create_tables([Applicant, Mentor, School, City, InterviewSlot], safe=True)
