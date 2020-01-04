from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
from .contact import ContForm
from .survey import Form
from flask import send_file
from flask_mail import Mail


app = Flask(__name__)
mail = Mail()
Bootstrap(app)
app.config['SECRET_KEY'] = 'oratoroeuaroupadoreideroma123'


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'irishousingproject@gmail.com'
app.config["MAIL_PASSWORD"] = 'irish_housing2020'
 
mail.init_app(app)

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

@app.route('/Contact', methods=['GET','POST'])
def Contact():
    form = ContForm()
    if request.method == 'POST':
        if form.validate() == True:
            flash('All fields are required.')
            return render_template('Contact.html', form=form)
        else:
            flash
            return render_template('Contact.html', success=True)
 
    elif request.method == 'GET':
        return render_template('Contact.html', form=form)

    
@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "\\4thSemestre\\AssignmentBreakdown\Paper\HouseMarket_09_12.docx";
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run()
