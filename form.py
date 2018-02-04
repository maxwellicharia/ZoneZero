from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, validators, IntegerField, SubmitField
# importing necessary fields and validators for the form


class NoteCreate(FlaskForm):  # class with all the required fields for creating notes

    note_subject = StringField("Note Subject",
                               [validators.DataRequired(message="Kindly input the Subject of your note")])
    note_name = StringField("Note Name", [validators.DataRequired(message="Kindly input the name of your note")])
    note_content = TextAreaField("Note Content", [validators.DataRequired(message="Content required")])
    submit = SubmitField("Create Note")


class NoteUpdate(FlaskForm):
    id = IntegerField('Note ID', [validators.DataRequired(message='Note Id needed!')])
    note_subject = StringField("Note Subject",
                               [validators.DataRequired(message="Kindly input the Subject of your note")])
    note_name = StringField("Note Name", [validators.DataRequired(message="Kindly input the name of your note")])
    note_content = TextAreaField("Note Content", [validators.DataRequired(message="Content required")])
    submit = SubmitField("Create Note")


class NoteID(FlaskForm):
    id = IntegerField('Note ID', [validators.DataRequired(message='Note Id needed!')])
