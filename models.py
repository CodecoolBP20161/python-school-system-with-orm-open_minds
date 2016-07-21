from peewee import *

# This is useful, after we pushed the final version
# db_name = input("Give me your database name: ")
# user_name = input("Give me your user name: ")

# This is the test version for us:
answer = input("Give me the username: ")
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
    status = CharField()


class Mentor(BaseModel):

    first_name = CharField()
    last_name = CharField()
    school_id = IntegerField()
