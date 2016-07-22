from peewee import *

""" The tables are based on these models. """


db_name = input("Give me your database name: ")
user_name = input("Give me your user name: ")

db = PostgresqlDatabase(db_name, user=user_name)


class BaseModel(Model):
    """ A base model that will use our Postgresql database. """
    class Meta:
        database = db


class City(BaseModel):
    """  City table based on City model. """
    name = CharField()
    nearest_school = CharField()


class School(BaseModel):
    """  School table based on School model. """
    name = CharField()
    city = CharField()


class Applicant(BaseModel):
    """  Applicant table based on Applicant model. """
    application_code = CharField(null=True, unique=True)
    first_name = CharField()
    last_name = CharField()
    year_of_birth = IntegerField()
    gender = CharField()
    city = CharField()
    assigned_school = CharField(null=True)
    status = CharField()

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return "Name: {}\nApplicant code: {}\nYear of birth: {}\nGender: {}\n\
        City: {}\nSchool: {}\nStatus: {}\n".format(full_name, self.application_code, self.year_of_birth,
                                                   self.gender, self.city, self.assigned_school, self.status)


class Mentor(BaseModel):
    """  Mentor table based on Mentor model. """
    first_name = CharField()
    last_name = CharField()
    school_id = IntegerField()


class InterviewSlot(BaseModel):
    """  InterviewSlot table based on InterviewSlot model. """
    date_time = DateTimeField()
    duration = IntegerField()
    mentor = CharField()
    applicant = CharField(null=True, unique=True)
    school_name = CharField()
