from peewee import *
from db_init import psql_db


class BaseModel(Model):
    """ A base model that will use our Postgresql database. """
    class Meta:
        database = psql_db
