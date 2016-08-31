from peewee import *
# from db_controller import psql_db

psql_db = PostgresqlDatabase('codecool-palko')


class BaseModel(Model):
    class Meta:
        database = psql_db


class Applicant(BaseModel):
    # application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    year_of_birth = IntegerField()
    gender = CharField()
    # city = CharField()
    # status = CharField()

    @staticmethod
    def add_applicants(data):
        for applicant in data:
            Applicant.create(first_name=applicant['first_name'],
                             last_name=applicant['last_name'],
                             email=applicant['email'],
                             year_of_birth=applicant['year_of_birth'],
                             gender=applicant['gender'],
                             city=applicant['city']
                             )
