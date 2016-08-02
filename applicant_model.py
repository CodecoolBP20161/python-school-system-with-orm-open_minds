from models import BaseModel


class Applicant(BaseModel):
    """  Applicant table based on Applicant model. """
    application_code = CharField(null=True, unique=True)
    first_name = CharField()
    last_name = CharField()
    year_of_birth = IntegerField()
    gender = CharField()
    city = CharField()
    assigned_school = ForeignKeyField(School, related_name='applicants', null=True)
    status = CharField()

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return "Name: {}\nApplicant code: {}\nYear of birth: {}\nGender: {}\nCity: {}\nSchool: {}\nStatus: {}\n".format\
            (full_name, self.application_code, self.year_of_birth,
             self.gender, self.city, self.assigned_school, self.status)

