from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from form import Form
from models import Models

# import necessary modules for use

app = Flask(__name__)
Bootstrap(app)
# app.config.from_object(__name__)
app.secret_key = "My Secret Key"

# the methods GET and POST are used to determine if content is received or being submitted

# render_template returns the HTML file that has been defined
# in the templates folder that is automatically detected

# form=form generates the form required as the HTML file is rendered


@app.route('/', methods=['GET', 'POST'])
# root route that the user will see after been authenticated in CAS
def dash():
    if request.method == 'GET':
        return render_template('dash.html')


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
            createdb.create()
            return render_template('success.html', create=True)


@app.route('/update', methods=['GET', 'POST'])
def update():
    return render_template('update.html')


@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template('view.html')


@app.route('/delete')
def delete():
    return render_template('delete.html')


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')
