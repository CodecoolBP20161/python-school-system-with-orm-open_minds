from peewee import *
from db_controller import psql_db


class BaseModel(Model):
    """ A base model that will use our Postgresql database. """
    class Meta:
        database = psql_db
