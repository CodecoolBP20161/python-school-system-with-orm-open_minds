from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from applicant_model import Applicant
from mentor_model import Mentor
from validate_email import validate_email

app = Flask(__name__)

app.config.update(dict(
   SECRET_KEY='development key',
   USERNAME='admin',
   PASSWORD='default'
))
app.config.from_envvar('SCHOOLSYSTEM_SETTINGS', silent=True)


@app.route('/')
def show_main_page():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """login to the app"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('show_adminmenu'))
    return render_template('login.html', error=error, title="Login")


@app.route('/logout')
def logout():
    """logout from the app"""
    session.pop('logged_in', None)
    flash('You logged out')
    return redirect(url_for('login'))


# shows the signup form - writing data to database happens in an other function
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html', title='Signup')


@app.route('/add', methods=['POST'])
def add_entry():
    if request.method == 'POST':
        data = [dict(request.form.items())]
        if data[0]['first_name'].isalpha() is False:
            flash("Invalid first name!")
        elif data[0]['last_name'].isalpha() is False:
            flash("Invalid last name!")
        elif validate_email(data[0]['email']) is False:
            flash("Invalid email!")
        else:
            data[0]['application_code'] = None
            data[0]['status'] = 'new'
            data[0]['assigned_school'] = None
            Applicant.applicants = data
            Applicant.add_applicants()
            Applicant.finding_city()
            Applicant.set_app_code()
            Applicant.assign_interview_slot()
            flash('Your signup has been submitted!')
    return redirect(url_for('signup'))


# shows adminmenu (login required)
@app.route('/adminmenu')
def show_adminmenu():
    if session.get('logged_in'):
        return render_template('adminmenu.html', title='Admin Menu')
    else:
        return redirect(url_for('login'))


# shows the filtering menu (login required), filtering uses html form(s)
@app.route('/filtering')
def show_filtering():
    if session.get('logged_in'):
        return render_template('filtering.html', title='Filters')
    else:
        return redirect(url_for('login'))


@app.route('/filtering/apply', methods=['POST'])
def handle_filters():
    if session.get('logged_in'):
        if request.method == 'POST':
            data = dict(request.form.items())
            print(data)
            if data['filtering'] == 'first_name':
                for applicant in Applicant.select().where(Applicant.first_name.contains(data['search'])):
                    print(applicant)
            elif data['filtering'] == 'last_name':
                for applicant in Applicant.select().where(Applicant.last_name.contains(data['search'])):
                    print(applicant)
            elif data['filtering'] == 'email':
                for applicant in Applicant.select().where(Applicant.email.contains(data['search'])):
                    print(applicant)
            elif data['filtering'] == 'year_of_birth':
                for applicant in Applicant.select().where(Applicant.year_of_birth == data['search']):
                    print(applicant)
            elif data['filtering'] == 'city':
                for applicant in Applicant.select().where(Applicant.city == data['search']):
                    print(applicant)
            elif data['filtering'] == 'mentor_id':
                for mentor in Mentor.select().where(Mentor.id == data['search']):
                    for element in mentor.interviews:
                        print(element.applicants.get())
            elif data['filtering'] == 'school':
                for applicant in Applicant.select().where(Applicant.assigned_school == data['search']):
                    print(applicant)
            elif data['filtering'] == 'status':
                for applicant in Applicant.select().where(Applicant.status.contains(data['search'])):
                    print(applicant)
            return redirect(url_for('show_data', filter=data['filtering']))
    else:
        return redirect(url_for('login'))


# shows data according to the selected filter
@app.route('/filtering/<filter>')
def show_data(filter):
    if session.get('logged_in'):
        return render_template('list.html', filter=filter, title='Filtered by ' + filter.title())
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
