from peewee import *

""" Tables are based on these models. """


db_name = input("Give me your database name: ")
user_name = input("Give me your user name: ")

db = PostgresqlDatabase(db_name, user=user_name)


class BaseModel(Model):
    """ A base model that will use our Postgresql database. """
    class Meta:
        database = db
