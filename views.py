import ssl

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_cas import CAS, login_required

from form import Form
from models import Models

# import necessary modules for use

app = Flask(__name__)
Bootstrap(app)
ssl._create_default_https_context = ssl._create_unverified_context
CAS(app, '/cas')
app.config['CAS_SERVER'] = 'https://127.0.0.1:8443/cas'
app.config['CAS_AFTER_LOGIN'] = 'dash'
app.config['CAS_ATTRIBUTES'] = ""
app.secret_key = "My Secret Key"


class Routes:
    def __init__(self):
        pass

    # the methods GET and POST are used to determine if content is received or being submitted

    # render_template returns the HTML file that has been defined
    # in the templates folder that is automatically detected

    # form=form generates the form required as the HTML file is rendered

    @app.route('/', methods=['GET', 'POST'])
    def root():
        return render_template('welcome.html', norm=True)

    @app.route('/cas/login', methods=['GET', 'POST'])
    def login():
        pass

    @login_required
    @app.route('/cas/logout', methods=['GET', 'POST'])
    def logout():
        pass

    @login_required
    @app.route('/dash', methods=['GET', 'POST'])
    # root route that the user will see after been authenticated in CAS
    def dash():
        return render_template('dash.html')

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
                db = Models()
                db.create()

                subject = request.form['notesubject']
                name = request.form['notename']
                content = request.form['notecontent']

                db.insert(subject, name, content)
                return render_template('success.html', create=True)

    @login_required
    @app.route('/update', methods=['GET', 'POST'])
    def update():
        return render_template('update.html')

    @login_required
    @app.route('/view', methods=['GET', 'POST'])
    def view():
        db = Models()
        rows = db.cur.fetchall()
        return render_template('view.html', rows=rows)

    @login_required
    @app.route('/success', methods=['GET', 'POST'])
    def success():
        return render_template('success.html')
