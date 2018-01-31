from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, validators, DateField, SubmitField
# importing necessary fields and validators for the form


class Form(FlaskForm):  # class with all the required fields for the form

    notesubject = StringField("Note Subject", [validators.DataRequired(message="Kindly input the Subject of your note")])
    notename = StringField("Note Name", [validators.DataRequired(message="Kindly input the name of your note")])
    notecontent = TextAreaField("Note Content", [validators.DataRequired(message="Content required")])
    submit = SubmitField("Create Note")
