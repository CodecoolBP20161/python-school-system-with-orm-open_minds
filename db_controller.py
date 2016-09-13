from peewee import *


def init_db():
    try:
        with open('db.nfo') as f:
           db_name = f.read()
    except FileNotFoundError:
        with open('db.nfo', 'w') as f:
            db_name = f.write(input("What's name your database?\n"))
    return db_name
init_db()
psql_db = PostgresqlDatabase(init_db())
psql_db.connect()


def create_table():
    from model_cityl import City
    from model_school import School
    from model_mentor import Mentor
    from model_applicant import Applicant
    from interviewslot_model import InterviewSlot

    psql_db.drop_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)
    psql_db.create_tables([School, City, Mentor, Applicant, InterviewSlot], safe=True)


def signup_db_query(data):
    from model_applicant import Applicant

    data[0]['application_code'] = None
    data[0]['status'] = 'new'
    data[0]['assigned_school'] = None
    Applicant.applicants = data
    Applicant.add_applicants()
    Applicant.finding_city()
    Applicant.set_app_code()
    Applicant.assign_interview_slot()


def filter_db_query(data):
    from model_applicant import Applicant
    from model_mentor import Mentor
    result = []
    try:
        if data['search'] == '':
            for applicant in Applicant.select():
                result.append(applicant)
            return result
        else:
            if data['filtering'] == 'name':
                for applicant in Applicant.select().where(
                                Applicant.first_name.contains(data['search']) or Applicant.last_name.contains(
                                data['search'])):
                                result.append(applicant)
            elif data['filtering'] == 'email':
                for applicant in Applicant.select().where(Applicant.email.contains(data['search'])):
                    result.append(applicant)
            elif data['filtering'] == 'year_of_birth':
                for applicant in Applicant.select().where(Applicant.year_of_birth == data['search']):
                    result.append(applicant)
            elif data['filtering'] == 'city':
                for applicant in Applicant.select().where(Applicant.city == data['search']):
                    result.append(applicant)
            elif data['filtering'] == 'mentor_id':
                for mentor in Mentor.select().where(Mentor.id == data['search']):
                    for element in mentor.interviews:
                        result.append(element.applicants.get())
            elif data['filtering'] == 'school':
                for applicant in Applicant.select().where(Applicant.assigned_school == data['search']):
                    result.append(applicant)
            elif data['filtering'] == 'status':
                for applicant in Applicant.select().where(Applicant.status.contains(data['search'])):
                    result.append(applicant)
            return result
    except KeyError:
        # If the user don't choose filter, but the keyword is given.
        return
