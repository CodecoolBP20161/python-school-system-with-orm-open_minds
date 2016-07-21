# Write a new script which detects unreserved interview slots and reserves an interview slot for the applicant
from models import *

applicants = {}


def check_reserved_interviews():
    for applicant in Applicant.select():
        applicants[applicant.application_code] = applicant.assigned_school
    for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
        if interview.applicant in applicants:
            del applicants[interview.applicant]


def interview_slot_handling():
    for element in applicants:
        for interview in InterviewSlot.select().where(InterviewSlot.applicant == None):
            if interview.school_name == applicants[element]:
                interview.applicant = element
                interview.save()
                break


def find_applicants_without_slot():
    for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
        print(interview.applicant)
        try:
            del applicants[interview.applicant]
        except KeyError:
            pass

    for element in applicants:
        print("Unfortunately we haven't free interview slot currently for {}".format(element))
