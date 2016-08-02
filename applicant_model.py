from models import *
from school_model import School


class Applicant(BaseModel):
    """  Applicant table based on Applicant model. """
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    year_of_birth = IntegerField()
    gender = CharField()
    city = CharField()
    assigned_school = ForeignKeyField(School, related_name='applicants', null=True)
    status = CharField()

    applicants = [
        {'application_code': 'thc420',
         'first_name': 'Bob',
         'last_name': 'Marley',
         'year_of_birth': 1966,
         'gender': 'male',
         'city': 'Jamaica',
         'assigned_school': 'Codecool Budapest',
         'status': 'accepted'},

        {'application_code': 'dev666',
         'first_name': 'Devil',
         'last_name': 'Lawyer',
         'year_of_birth': 1966,
         'gender': 'male',
         'city': 'Hell',
         'assigned_school': 'Codecool Budapest',
         'status': 'rejected'},

        {'application_code': 'nir333',
         'first_name': 'Curt',
         'last_name': 'Cobain',
         'year_of_birth': 1967,
         'gender': 'male',
         'city': 'Rome',
         'assigned_school': 'Codecool Budapest',
         'status': 'in progress'},

        {'application_code': None,
         'first_name': 'Pam',
         'last_name': 'Pam',
         'year_of_birth': 1993,
         'gender': 'notsure',
         'city': 'Győr',
         'assigned_school': None,
         'status': 'new'},

        {'application_code': None,
         'first_name': 'Frodo',
         'last_name': 'Baggins',
         'year_of_birth': 2000,
         'gender': 'male',
         'city': 'Debrecen',
         'assigned_school': None,
         'status': 'new'},

        {'application_code': None,
         'first_name': 'Elvis',
         'last_name': 'Presley',
         'year_of_birth': 1935,
         'gender': 'male',
         'city': 'Barcelona',
         'assigned_school': None,
         'status': 'new'},

        {'application_code': None,
         'first_name': 'Andreste',
         'last_name': 'Éimhear',
         'year_of_birth': 1909,
         'gender': 'female',
         'city': 'Budapest',
         'assigned_school': None,
         'status': 'new'},

        {'application_code': None,
         'first_name': 'Jean',
         'last_name': 'D\'Arc',
         'year_of_birth': 1412,
         'gender': 'female',
         'city': 'Paris',
         'assigned_school': None,
         'status': 'new'},

        {'application_code': None,
         'first_name': 'Krystyna',
         'last_name': 'Rudaski',
         'year_of_birth': 1980,
         'gender': 'female',
         'city': 'Krakow',
         'assigned_school': None,
         'status': 'new'}
    ]

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return "Name: {}\nApplicant code: {}\nYear of birth: {}\nGender: {}\nCity: {}\nSchool: {}\nStatus: {}\n".format\
            (full_name, self.application_code, self.year_of_birth,
             self.gender, self.city, self.assigned_school, self.status)

    @staticmethod
    def add_applicants():
        for applicant in Applicant.applicants:
            Applicant.create(application_code=applicant['application_code'],
                             first_name=applicant['first_name'],
                             last_name=applicant['last_name'],
                             year_of_birth=applicant['year_of_birth'],
                             gender=applicant['gender'],
                             city=applicant['city'],
                             assigned_school=School.select().where(School.name == applicant['assigned_school']),
                             status=applicant['status']
                             )

    @classmethod
    def find_missing_app_code(cls):
        return Applicant.select().where(Applicant.application_code >> None)

    @classmethod
    def find_missing_school(cls):
        return Applicant.select().where(Applicant.assigned_school >> None)

    @classmethod
    def finding_city(cls):
        """Find nearest_school for applicants"""
        applicants = cls.find_missing_school()
        for applicant in applicants:
            applicant.set_city()

    def set_city(self):
        self.school = City.select(City.nearest_school).where(City.name == self.city)
        self.save()

    @classmethod
    def set_app_code(cls):
        pass

# print(Applicant.find_missing_app_code())
