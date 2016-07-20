
from peewee import *
import uuid
from models import *


new_applicants = {}
existing_application_codes = []


def find_new_applicants():
    for applicant in Applicant.select():
        new_applicants[applicant.id] = applicant.application_code


def get_ids():
    for applicant in Applicant:
        existing_application_codes.append(applicant.application_code)


def app_code_generator():
    id_temp = str(uuid.uuid4())[:6]
    if id_temp not in existing_ids:
        return id_temp
