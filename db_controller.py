from peewee import *

db_name = ""

psql_db = PostgresqlDatabase(db_name)
psql_db.connect()


def create_table():
    from city_model import City
    from school_model import School
    from mentor_model import Mentor
    from applicant_model import Applicant
    from interviewslot_model import InterviewSlot

    psql_db.drop_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)
    psql_db.create_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)