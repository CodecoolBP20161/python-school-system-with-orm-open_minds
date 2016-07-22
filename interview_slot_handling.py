from models import *


class InterviewHandling:

    applicants = {}

    @staticmethod
    def interview_handling():
        # Collects applicants and fills them into applicants{}
        # Example: applicants[key] = application_code, applicants[value] = assigned_school
        for applicant in Applicant.select():
            InterviewHandling.applicants[applicant.application_code] = applicant.assigned_school
        # Detects students already assigned to an interview and deletes them from the dictionary
        for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
            if interview.applicant in InterviewHandling.applicants:
                del InterviewHandling.applicants[interview.applicant]

        # Assign students to free interview slots one by one
        # The break stops the subloop and starts the assigning again with an other student
        for element in InterviewHandling.applicants:
            for interview in InterviewSlot.select().where(InterviewSlot.applicant == None):
                if interview.school_name == InterviewHandling.applicants[element]:
                    interview.applicant = element
                    interview.save()
                    break

        # Checks whether an applicant is assigned to an interview
        # In case they are, deletes them from the dictionary
        for interview in InterviewSlot.select().where(InterviewSlot.applicant != None):
            try:
                del InterviewHandling.applicants[interview.applicant]
            except KeyError:
                pass

        # Prints students who haven't been assigned to an interview
        for element in InterviewHandling.applicants:
            print("Unfortunately, we have no free interview slot left currently for {}".format(element))
