from peewee import *
from model import Applicant, psql_db

psql_db.connect()

try:
    psql_db.create_table(Applicant)
    print("Table created.")
    # If the table is exist, don't try create again.
except ProgrammingError:
    print("Table already exist.")
    pass
