from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, Email
from wtforms import SelectField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
#from contact import ContForm
from survey import Form
from flask import send_file
from flask_mail import Mail, Message


app = Flask(__name__)
mail = Mail()
Bootstrap(app)
app.config['SECRET_KEY'] = 'oratoroeuaroupadoreideroma123'


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'irishousingproject@gmail.com'
app.config["MAIL_PASSWORD"] = 'irish_housingProject19'
 
mail.init_app(app)


class ContForm(Form):
    name = TextField("Name", [DataRequired()])
    email = StringField('Email address', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    subject = TextField("Subject", [DataRequired()])
    message = TextAreaField("Message", [DataRequired()])
    submit = SubmitField("Send")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    if request.method == 'POST':
        if form.validate_on_submit():
            flash(u'Something went wrong!', 'success')
            
        else:
            flash(u'Thank you for your collaboration!', 'error')
        return redirect(url_for('index'))
    return render_template('index1.html', form=form)

@app.route('/About', methods=['GET','POST'])
def About():
    return render_template('About1.html')

@app.route('/Design', methods=['GET','POST'])
def Design():
    return render_template('Design.html')

@app.route('/Contact', methods=['GET','POST'])
def Contact():
    form = ContForm()
    if request.method == 'POST':
        if form.validate() == True:
            flash('All fields are required.')
            return render_template('Contact.html', form=form)
        else:
            msg = Message('Hello',
            sender=('Myself', 'raphaelreinhold@hotmail.com'),
            recipients=['irishousingproject@gmail.com'])
            msg.body = "testing"
            mail.send(msg)

            flash('not sure what to write here just yet')
            return render_template('Contact.html', success=True)
 
    elif request.method == 'GET':
        return render_template('Contact.html', form=form)

    
@app.route('/file-downloads/')
def file_downloads():
	try:
		return render_template('downloads.html')
	except Exception as e:
		return str(e)

@app.route('/return-files/')
def return_files():
	try:
		return send_file('C:/Users/rapha/Documents/College/webappProject/webAppIrishHousing/static/toDownload/IrishHousingProject.pdf', attachment_filename='IrishHousingProject.pdf')
	except Exception as e:
		return str(e)

@app.route('/return-files1/')
def return_files1():
    try:
        return redirect('https://github.com/Reinhold83/webAppIrishHousing.git')
    except Exception as e:
		    return str(e)


if __name__ == '__main__':
    app.run()