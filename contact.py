from wtforms import Form, TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, Email

class ContForm(Form):
    name = TextField("Name", [DataRequired()])
    email = StringField('Email address', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    subject = TextField("Subject", [DataRequired()])
    message = TextAreaField("Message", [DataRequired()])
    submit = SubmitField("Send")