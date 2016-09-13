def applicant_signup(data):
    from model_applicant import Applicant

    data[0]['application_code'] = None
    data[0]['status'] = 'new'
    data[0]['assigned_school'] = None
    Applicant.applicants = data
    Applicant.add_applicants()
    Applicant.finding_city()
    Applicant.set_app_code()
    Applicant.assign_interview_slot()


def admin_filter(data):
    from model_applicant import Applicant
    from model_mentor import Mentor
    result = []
    try:
        if data['search'] == '':
            for applicant in Applicant.select():
                result.append(applicant)
            return result
        else:
            if data['filtering'] == 'name':
                for applicant in Applicant.select().where(
                                Applicant.first_name.contains(data['search']) or Applicant.last_name.contains(
                                data['search'])):
                                result.append(applicant)
            elif data['filtering'] == 'email':
                for applicant in Applicant.select().where(Applicant.email.contains(data['search'])):
                    result.append(applicant)
            elif data['filtering'] == 'year_of_birth':
                for applicant in Applicant.select().where(Applicant.year_of_birth == data['search']):
                    result.append(applicant)
            elif data['filtering'] == 'city':
                for applicant in Applicant.select().where(Applicant.city == data['search']):
                    result.append(applicant)
            elif data['filtering'] == 'mentor_id':
                for mentor in Mentor.select().where(Mentor.id == data['search']):
                    for element in mentor.interviews:
                        result.append(element.applicants.get())
            elif data['filtering'] == 'school':
                for applicant in Applicant.select().where(Applicant.assigned_school == data['search']):
                    result.append(applicant)
            elif data['filtering'] == 'status':
                for applicant in Applicant.select().where(Applicant.status.contains(data['search'])):
                    result.append(applicant)
            return result
    except KeyError:
        # If the user don't choose filter, but the keyword is given.
        return
