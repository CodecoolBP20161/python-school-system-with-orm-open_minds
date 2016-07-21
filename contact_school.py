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

    for element in result:
        print("The {} make contact with {}".format(result[element], element))

get_nearest_school()
