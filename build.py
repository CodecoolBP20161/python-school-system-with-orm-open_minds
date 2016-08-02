from models import *
from school_model import School


db = PostgresqlDatabase("")
db.connect()
db.drop_tables([School], safe=True)
db.create_tables([School], safe=True)

School.add_schools()