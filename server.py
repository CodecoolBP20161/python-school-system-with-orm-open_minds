from flask import Flask, render_template, redirect, request, url_for, flash
from model import Applicant

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
            return redirect(url_for('list_entries'))
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
        print(data)
        Applicant.add_applicants(data)
    flash('your signup has been submitted!')
    return redirect(url_for('signup'))


# shows adminmenu (login required)
@app.route('/adminmenu')
def show_adminmenu():
    if session.get('logged_in'):
        return render_template('adminmenu.html', title='Admin')
    else:
        return redirect(url_for('login'))


# shows the filtering menu (login required), filtering uses html form(s)
@app.route('/filtering')
def show_filtering():
    if session.get('logged_in'):
        return render_template('filtering.html', title='Filtering')
    else:
        return redirect(url_for('login'))


# shows data according to the selected filter
@app.route('/filtering/<filter>')
def show_data(filter):
    if session.get('logged_in'):
        return render_template('list.html', title='filter')
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
