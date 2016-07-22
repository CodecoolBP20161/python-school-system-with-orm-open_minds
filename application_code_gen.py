from models import *
import uuid

existing_application_codes = []


# Fills the existing_application_codes list.
def get_application_code():
    for applicant in Applicant.select():
        existing_application_codes.append(applicant.application_code)
    return existing_application_codes


# Generates a new ID and checks whether it is already assigned. If it is, the function runs again.
def app_code_generator():
    new_code = str(uuid.uuid4())[:6]
    if new_code not in get_application_code():
        return new_code
    else:
        return app_code_generator()


# Assigns the generated application code to applicants and saves the table
def assign_app_codes():
    for applicant in Applicant.select().where(Applicant.application_code == None):
            applicant.application_code = app_code_generator()
            applicant.save()
