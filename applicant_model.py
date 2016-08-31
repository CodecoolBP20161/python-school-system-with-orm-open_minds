from basemodel import *
from school_model import School
from city_model import City
from interviewslot_model import InterviewSlot
from mentor_model import Mentor
from email_class import Email
import uuid


class Applicant(BaseModel):
    """  Applicant table based on Applicant model. """
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    year_of_birth = IntegerField()
    gender = CharField()
    city = CharField()
    assigned_school = ForeignKeyField(School, related_name='applicants', null=True)
    interview_slot = ForeignKeyField(InterviewSlot, related_name='applicants', null=True)
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

    existing_application_codes = []

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return "Name: {}\nApplicant code: {}\nYear of birth: {}\nGender: {}\nCity: {}\nSchool: {}\nStatus: {}\n".format\
            (full_name, self.application_code, self.year_of_birth,
             self.gender, self.city, self.assigned_school.name, self.status)

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
            applicant.assigned_school = City.select(City.nearest_school).where(City.name == Applicant.city)
            applicant.save()

    @classmethod
    def app_code_gen(cls):
        new_code = str(uuid.uuid4())[:6]
        if new_code not in Applicant.existing_application_codes:
            Applicant.existing_application_codes.append(new_code)
            return new_code
        else:
            app_code_gen()

    @classmethod
    def set_app_code(cls):
        applicants = Applicant.find_missing_app_code()
        for applicant in applicants:
            applicant.application_code = Applicant.app_code_gen()
            applicant.status = 'in progress'
            applicant.save()
        cls.find_handled_applications()

    @classmethod
    def find_empty_interview_slot(cls):
        return Applicant.select().where(Applicant.interview_slot >> None)

    @classmethod
    def assign_interview_slot(cls):
        applicants = cls.find_empty_interview_slot()
        for applicant in applicants:
            applicant.set_interview_slot()
        cls.find_applicant_interviews()

    def set_interview_slot(self):
        query = (InterviewSlot.select(InterviewSlot, Mentor)
                 .join(Mentor).where(InterviewSlot.free, Mentor.school_id == self.assigned_school))
        try:
            slot = [i for i in query][0]
            slot.free = False
            slot.save()
            self.interview_slot = slot
            self.save()
        except IndexError:
            if self.status == 'in progress':
                print('No more free interview slots for {}'.format(self.application_code.upper()))
            else:
                pass

    @staticmethod
    def find_handled_applications():
        applicants = Applicant.select().where(Applicant.status == 'in progress')

        for applicant in applicants:
            email_subject = 'Your Codecool application has been handled!'
            email_body = "Hi {},\n\nThank you for applying to Codecool!\n\n\
Your have been assigned to {}.\nYour application code is {}.\n\n\
We will contact you again soon with the details of your personal interview!\n\n\
Cheers,\nMentors of {}".format(applicant.first_name, applicant.assigned_school.name,
                               applicant.application_code, applicant.assigned_school.name)

            print('Sending email with assigned school and application code.')
            Email(user='', pwd='', to=[''],
                  subject=email_subject,
                  body=email_body).email_sender()

    @staticmethod
    def find_applicant_interviews():
        applicants = Applicant.select().where(Applicant.status == 'in progress')

        for applicant in applicants:
            email_subject = 'Your Codecool interview'
            email_body = "Hi {},\n\nYour personal interview will be in {} at {}. Your interviewer \
will be {} and the interview will take {} hours. Please bring your application code ({}) and some cookies :)\
\n\nCheers,\nMentors of {}".format(applicant.first_name,
                                   applicant.assigned_school.name,
                                   applicant.interview_slot.date_time,
                                   applicant.interview_slot.mentor.first_name +
                                   ' ' + applicant.interview_slot.mentor.last_name,
                                   applicant.interview_slot.duration,
                                   applicant.application_code,
                                   applicant.assigned_school.name
                                   )

            print('Sending email with information on assigned interview.')
            Email(user='', pwd='', to=[''],
                  subject=email_subject,
                  body=email_body).email_sender()
