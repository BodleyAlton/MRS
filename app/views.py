from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from models import *
from forms import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_Nurse')
def addNurse():
    nform=nurseForm()
    return render_template('create_nurse.html',form=nform)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        # if form.validate_on_submit():
        #     username=form.username.data
        #     password=form.password.data
        #     user=UserProfile.query.filter_by(username=username, password=password).first()
        #     print user
        #     login_user(user)
        #     flash("Login Successfull.",'success')
            return redirect(url_for("secure_page"))
    return render_template('login.html',form=form)

@app.route('/secure-page/')
#@login_required
def secure_page():
    return render_template('secure_page.html')

@app.route('/search',methods=["GET", "POST"])
def search():
    searchf = Search()
    if request.method=="POST":
        print "POST"
        #if searchf.validate_on_submit():
        diagnos=searchf.diagnosis.data
        fdate=searchf.fdate.data
        tdate=searchf.tdate.data
        print "Diagnosis: "+ diagnos
        print "FDATE: "+str(fdate)
        print "TDATE: "+str(tdate)
        searchd=[diagnos,fdate,tdate]
        return redirect(url_for('result',search=searchd))
    print "GET"
    return render_template('search.html',form=searchf)

@app.route('/result/<search>',methods=['GET','POST'])
def result(search):
    #patient= db.session.query(patient).filter_by(p_trn=userid)
    return render_template('viewprof.html')#,users=patient)
