
from peewee import *
import uuid
from models import *


existing_application_codes = []


def get_application_code():
    for applicant in Applicant.select():
        existing_application_codes.append(applicant.application_code)
    return existing_application_codes


def app_code_generator():
    new_code = str(uuid.uuid4())[:6]
    if new_code not in get_application_code():
        return new_code
    else:
        return app_code_generator()


def assign_app_codes():
    for applicant in Applicant.select().where(Applicant.application_code == None):
            applicant.application_code = app_code_generator()
            applicant.save()
