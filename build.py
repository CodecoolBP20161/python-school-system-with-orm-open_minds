from models import *
from school_model import School
from mentor_model import Mentor

db = PostgresqlDatabase("")
db.connect()
db.drop_tables([School, Mentor], safe=True)
db.create_tables([School, Mentor], safe=True)

School.add_schools()
Mentor.add_mentors()
