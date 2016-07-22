from models import *


class InterviewHandling:

    applicants = {}

    @staticmethod
    def interview_handling():
        # This collect the all applicants and organize into "applicants" dict.
        # Example: applicants[key] = application_code, applicants[value] = assigned_school
        for applicant in Applicant.select():
            InterviewHandling.applicants[applicant.application_code] = applicant.assigned_school
        # Who already have reserved interview slot delete them form the dictionary.
        for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
            if interview.applicant in InterviewHandling.applicants:
                del InterviewHandling.applicants[interview.applicant]

        # Who haven't reserved interview slot get a new appointment.
        # After that break the subloop and looking fo an other one.
        for element in InterviewHandling.applicants:
            for interview in InterviewSlot.select().where(InterviewSlot.applicant == None):
                if interview.school_name == InterviewHandling.applicants[element]:
                    interview.applicant = element
                    interview.save()
                    break

        # This checks the applicants who didn't get interview slot.
        # Then deletes the ones who has interview slot.
        for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
            try:
                del InterviewHandling.applicants[interview.applicant]
            except KeyError:
                pass

        # And print the dictionary element.
        for element in InterviewHandling.applicants:
            print("Unfortunately, we have no free interview slot left currently for {}".format(element))
