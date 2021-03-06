from flask import Flask, request, session, redirect, url_for, render_template, flash
from controller_applicant import applicant_signup, admin_filter


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
            flash('Invalid username, try again!')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Invalid password, try again!')
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('show_filtering'))

    return redirect(url_for('show_main_page'))
    # return render_template('login.html', error=error, title="Login")


@app.route('/logout')
def logout():
    """logout from the app"""
    session.pop('logged_in', None)
    flash('You logged out')
    return redirect(url_for('show_main_page'))


# handles the signup form
@app.route('/add', methods=['POST'])
def add_entry():
    if request.method == 'POST':
        data = [dict(request.form.items())]
        applicant_signup(data)
        flash('Your signup has been submitted!')
    return redirect(url_for('show_main_page'))


# shows the filtering menu (login required), filtering uses html form(s)
@app.route('/filtering')
def show_filtering():
    if session.get('logged_in'):
        return render_template('filtering.html', title='Filters')
    else:
        return redirect(url_for('show_main_page'))


@app.route('/filtering/apply', methods=['POST'])
def handle_filters():
    if session.get('logged_in'):
        if request.method == 'POST':
            data = dict(request.form.items())
            try:
                applicant_list = admin_filter(data)
                if applicant_list is None:
                    flash("Please choose a filter!")
                    return redirect(url_for('show_filtering'))
                else:
                    return render_template("list.html", applicant_list=applicant_list)
            except ValueError:
                return redirect(url_for('show_filtering'))
    else:
        return redirect(url_for('show_main_page'))


if __name__ == "__main__":
    app.run(debug=True)
