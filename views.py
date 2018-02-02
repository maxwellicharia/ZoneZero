import ssl

from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_cas import CAS, login_required

from form import Form
from models import Models

# import necessary modules for use

app = Flask(__name__)
Bootstrap(app)

ssl._create_default_https_context = ssl._create_unverified_context

cas = CAS(app, '/cas')

app.config['CAS_SERVER'] = 'https://127.0.0.1:8443/cas/login/'
app.config['CAS_AFTER_LOGIN'] = '/dash'
app.config['CAS_ATTRIBUTES'] = ""
app.config['CAS_AFTER_LOGOUT'] = '/logout'
# with app.app_context():
#     # MySQL configurations
#     app.config['MYSQL_DATABASE_USER'] = 'notes'
#     app.config['MYSQL_DATABASE_PASSWORD'] = 'Not3s_db'
#     app.config['MYSQL_DATABASE_DB'] = 'notes'
#     app.config['MYSQL_DATABASE_HOST'] = '10.55.17.80:3306'
#     mysql = MySQL()
#     mysql.init_app(app)

# app.config.from_object(__name__)
app.secret_key = "My Secret Key"

# the methods GET and POST are used to determine if content is received or being submitted

# render_template returns the HTML file that has been defined
# in the templates folder that is automatically detected

# form=form generates the form required as the HTML file is rendered


# @app.route('/logout', methods=['GET', 'POST'])
# @logout
# def logout
#     return render_template('welcome.html')

@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('welcome.html')


@login_required
@app.route('/dash', methods=['GET', 'POST'])
# root route that the user will see after been authenticated in CAS
def dash():
    return render_template('dash.html')


@login_required
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return url_for('cas.logout')


@login_required
@app.route('/create', methods=['GET', 'POST'])
# route that coordinates the creation of a new note
def create():
    form = Form(request.form)  # instantiating form to use the forms defined from the Form class in form.py

    if request.method == 'GET':
        return render_template('create.html', form=form)
    else:
        if not form.validate_on_submit():  # making sure that the form is validated before submission
            return render_template('create.html', form=form)
        else:
            createdb = Models()
            subject = request.form['notesubject']
            name = request.form['notename']
            content = request.form['notecontent']
            createdb.insert(subject, name, content)
            return render_template('success.html', create=True)


@login_required
@app.route('/update', methods=['GET', 'POST'])
def update():
    return render_template('update.html')


@login_required
@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template('view.html')


@login_required
@app.route('/delete')
def delete():
    return render_template('delete.html')


@login_required
@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')
