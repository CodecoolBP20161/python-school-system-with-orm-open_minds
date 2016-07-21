from peewee import *

# This is useful, after we pushed the final version
# db_name = input("Give me your database name: ")
# user_name = input("Give me your user name: ")

# This is the test version for us:
answer = "david"
db_name = answer
username = answer

db = PostgresqlDatabase(db_name, user=username)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class City(BaseModel):

    name = CharField()
    nearest_school = CharField()


class School(BaseModel):

    name = CharField()
    city = CharField()


class Applicant(BaseModel):

    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    year_of_birth = IntegerField()
    gender = CharField()
    city = CharField()
    assigned_school = CharField(null=True)
    status = CharField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Mentor(BaseModel):

    first_name = CharField()
    last_name = CharField()
    school_id = IntegerField()


class InterviewSlot(BaseModel):

    date_time = DateTimeField()
    duration = IntegerField()
    mentor = CharField()
    applicant = CharField(null=True)
    school_name = CharField()
