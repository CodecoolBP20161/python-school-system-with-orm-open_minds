from models import *

new_applicant_city = {}
nearest_school = {}
result = {}


def get_nearest_school():
    for applicant in Applicant.select().where(Applicant.status == 'new'):
        new_applicant_city[applicant.first_name] = applicant.city
    for city in City.select():
        nearest_school[city.name] = city.nearest_school

    for element in new_applicant_city:
        for city in nearest_school:
            if new_applicant_city[element] == city:
                result[element] = nearest_school[city]
    # print(result)

    for element in result:
        print("The {} made contact with {}".format(result[element], element))

    for applicant in Applicant.select().where(Applicant.status == 'new'):
        applicant.status = 'in progress'
        applicant.save()
        for element in result:
            # print(element, applicant.first_name)
            if element == applicant.first_name:
                applicant.assigned_school = result[element]
                applicant.save()
