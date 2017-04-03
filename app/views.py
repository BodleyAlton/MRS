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
        searchd=diagnos,fdate,tdate
        return redirect(url_for('result',diag=diagnos,fd=fdate,td=tdate))
    print "GET"
    return render_template('search.html',form=searchf)

@app.route('/result/<diag>,<fd>,<td>',methods=['GET','POST'])
def result(diag,fd,td):
    diags=diag
    #query for the nammes of patients with desease between fd  and td
    return render_template('viewprof.html',diags=diag)#,users=patient)

@app.route ('/alergy',methods=['GET','POST'])
def alergy():
    alergyf=Alergyform()
    if request.method=="POST":
        trn=alergyf.p_trn.data
        print trn
        #query for all alergy with trn
        return redirect(url_for('patient_alergy',patient=trn))
    return render_template('alergy.html',form=alergyf)

@app.route('/patient_alergy/<patient>')
def patient_alergy(patient):
    trnn=patient
    return render_template('pat_alergy.html',patient=trnn)

@app.route('/meds')
def meds():
    meds="Rahtid"#query for most alergic Medication
    return render_template('almeds.html',meds=meds)

@app.route ('/test',methods=['GET','POST'])
def test():
    test=Alergyform()
    if request.method=="POST":
        trn=test.p_trn.data
        print trn
        #query for all test results with trn
        return redirect(url_for('patient_test',tests=trn))
    return render_template('patientSearch.html',form=test)

@app.route('/tests/<tests>')
def patient_test(tests):
    trnn=tests
    return render_template('pat_test.html',tests=trnn)

@app.route('/patient-care',methods=['POST','GET'])
def patient_care():
    pat=Carefm()
    if request.method=='POST':
        p_trn=pat.p_trn.data
        date=pat.date.data
        nurse="NURSES"
        return redirect(url_for('nurse_care',nurses=nurse))
    return render_template('careSearch.html',form=pat)
@app.route('/nurse_care/<nurses>')
def nurse_care(nurses):
    nurse="Nurses"
    return render_template('nursecare.html',nurses=nurse)

@app.route('/interns')
def interns():
    interns="This intern treatred the most patients"#query for most alergic Medication
    return render_template('interns.html',intern=interns)
