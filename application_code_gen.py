
from peewee import *
import uuid
from models import *


existing_application_codes = []


def get_ids():
    for applicant in Applicant:
        existing_application_codes.append(applicant.application_code)
    return


def app_code_generator():
    new_code = str(uuid.uuid4())[:6]
    if new_code not in existing_application_codes:
        return new_code
    else:
        return app_code_generator()


def assign_app_codes():
    for applicant in Applicant.select():
        get_ids()
        applicant.update(application_code=app_code_generator()).where(applicant.status == 'new').execute()
        applicant.update(status='in progress').execute()

assign_app_codes()
