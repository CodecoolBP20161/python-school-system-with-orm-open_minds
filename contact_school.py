from models import *


class ContactSchool:

    new_applicant_city = {}
    nearest_school = {}
    result = {}

    @staticmethod
    def get_nearest_school():
        # Collects the new applicants and their city.
        # After that organizes into "new_applicant_city" dictionary.
        for applicant in Applicant.select().where(Applicant.status == 'new'):
            ContactSchool.new_applicant_city[applicant.first_name] = applicant.city
        # Collects all cities and the nearest schools assigned,
        # then organizes them into "nearest_school" dictionary.
        for city in City.select():
            ContactSchool.nearest_school[city.name] = city.nearest_school

        # Merges the two dictionaries.
        # Example: result[key] = application_code, applicants[value] = nearest_school
        for element in ContactSchool.new_applicant_city:
            for city in ContactSchool.nearest_school:
                if ContactSchool.new_applicant_city[element] == city:
                    ContactSchool.result[element] = ContactSchool.nearest_school[city]

        # Prints the "result" dictionary.
        for element in ContactSchool.result:
            print("{} have made contact with {}".format(ContactSchool.result[element], element))

        # Sets the applicants' status from 'new' to 'in progress'
        for applicant in Applicant.select().where(Applicant.status == 'new'):
            applicant.status = 'in progress'
            applicant.save()
            for element in ContactSchool.result:
                if element == applicant.first_name:
                    applicant.assigned_school = ContactSchool.result[element]
                    applicant.save()
