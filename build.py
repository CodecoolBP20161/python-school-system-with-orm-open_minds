from models import *
from school_model import School
from city_model import City
from mentor_model import Mentor
from applicant_model import Applicant
from interviewslot_model import InterviewSlot

db = PostgresqlDatabase("")
db.connect()
db.drop_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)
db.create_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)

School.add_schools()
Mentor.add_mentors()
InterviewSlot.add_interview_slot()
City.add_cities()
Applicant.add_applicants()
