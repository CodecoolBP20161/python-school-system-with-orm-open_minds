from models import *


class ContactSchool:

    new_applicant_city = {}
    nearest_school = {}
    result = {}

    @staticmethod
    def get_nearest_school():
        for applicant in Applicant.select().where(Applicant.status == 'new'):
            ContactSchool.new_applicant_city[applicant.first_name] = applicant.city
        for city in City.select():
            ContactSchool.nearest_school[city.name] = city.nearest_school

        for element in ContactSchool.new_applicant_city:
            for city in ContactSchool.nearest_school:
                if ContactSchool.new_applicant_city[element] == city:
                    ContactSchool.result[element] = ContactSchool.nearest_school[city]

        for element in ContactSchool.result:
            print("The {} made contact with {}".format(ContactSchool.result[element], element))

        for applicant in Applicant.select().where(Applicant.status == 'new'):
            applicant.status = 'in progress'
            applicant.save()
            for element in ContactSchool.result:
                if element == applicant.first_name:
                    applicant.assigned_school = ContactSchool.result[element]
                    applicant.save()
