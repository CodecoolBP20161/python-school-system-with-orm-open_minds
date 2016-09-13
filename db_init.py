from peewee import *


def init_db():
    try:
        with open('db.nfo') as f:
           db_name = f.read()
    except FileNotFoundError:
        with open('db.nfo', 'w') as f:
            db_name = f.write(input("What's name your database?\n"))
    return db_name


def create_table():
    from model.model_city import City
    from model.model_school import School
    from model.model_mentor import Mentor
    from model.model_applicant import Applicant
    from model.model_interviewslot import InterviewSlot

    psql_db.drop_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)
    psql_db.create_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)


psql_db = PostgresqlDatabase(init_db())
psql_db.connect()
