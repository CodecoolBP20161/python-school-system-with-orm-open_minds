# Write a new script which detects unreserved interview slots and reserves an interview slot for the applicant
from models import *


class InterviewHandling:

    applicants = {}

    @staticmethod
    def check_reserved_interviews():
        for applicant in Applicant.select():
            InterviewHandling.applicants[applicant.application_code] = applicant.assigned_school
        for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
            if interview.applicant in InterviewHandling.applicants:
                del InterviewHandling.applicants[interview.applicant]

    # @staticmethod
    # def interview_slot_handling():
        for element in InterviewHandling.applicants:
            for interview in InterviewSlot.select().where(InterviewSlot.applicant == None):
                if interview.school_name == InterviewHandling.applicants[element]:
                    interview.applicant = element
                    interview.save()
                    break

    # @staticmethod
    # def find_applicants_without_slot():
        for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
            try:
                del InterviewHandling.applicants[interview.applicant]
            except KeyError:
                pass

        for element in InterviewHandling.applicants:
            print("Unfortunately, we have no free interview slot left currently for {}".format(element))
