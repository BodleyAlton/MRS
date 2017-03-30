from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, IntegerField,PasswordField, DateField
from wtforms.validators import InputRequired

class patientsForm(FlaskForm):
    p_trn = IntegerField('TRN',validators=[InputRequired()])
    pf_name = StringField('First Name', validators=[InputRequired()])
    pl_name = StringField('Last Name', validators=[InputRequired()])
    dob = DateField ('D.O.B',format='%d/%m/%Y', validators=[InputRequired()])
    pcontact = StringField('Contact', validators=[InputRequired()])
    address_1 = StringField('Address 1', validators=[InputRequired()])
    address_2 = StringField('Address 2', validators=[InputRequired()])
    city  = StringField('City', validators=[InputRequired()])
    parish = StringField('Parish', validators=[InputRequired()])

class nurseForm(FlaskForm):
    nf_name= StringField('First Name', validators=[InputRequired()])
    nl_name= StringField('Last Name', validators=[InputRequired()])
    ncontact= IntegerField('Contact',validators=[InputRequired()])
    address_1=StringField('Address 1', validators=[InputRequired()])
    address_2=StringField('Address 2', validators=[InputRequired()])
    city= StringField('City', validators=[InputRequired()])
    parish= StringField('Parish', validators=[InputRequired()])
    type_=StringField('Type', validators=[InputRequired()])
    nemail= StringField('E-mail',validators=[InputRequired()])
    npassword= PasswordField('Password',validators=[InputRequired()])

class doctorForm(FlaskForm):
    df_name= StringField('First Name', validators=[InputRequired()])
    dcl_name= StringField('Last Name', validators=[InputRequired()])
    dcontact= IntegerField('Contact',validators=[InputRequired()])
    address_1=StringField('Address 1', validators=[InputRequired()])
    address_2=StringField('Address 2', validators=[InputRequired()])
    city= StringField('City', validators=[InputRequired()])
    parish= StringField('Parish', validators=[InputRequired()])
    type_=StringField('Type', validators=[InputRequired()])
    demail= StringField('E-mail',validators=[InputRequired()])
    dpassword= PasswordField('Password',validators=[InputRequired()])

class updateForm(FlaskForm):
    date = DateField ('D.O.B',format='%d/%m/%Y', validators=[InputRequired()])
    vitals_id= IntegerField('Vitals Id',validators=[InputRequired()])
    Reading= IntegerField('Reading',validators=[InputRequired()])
    d_eid = IntegerField('Doctor\'s ID',validators=[InputRequired()])
    bed_no = IntegerField('Patients Bed No.',validators=[InputRequired()])
    m_id= IntegerField('Medication ID',validators=[InputRequired()])

class phistoryForm(FlaskForm):
    code= StringField('Disease code', validators=[InputRequired()])
    p_trn = StringField('Patients TRN', validators=[InputRequired()])
    pro_id = StringField('Procedure ID', validators=[InputRequired()])
    t_id = StringField('Treatment ID', validators=[InputRequired()])
    tr_id= StringField('Test Result ID', validators=[InputRequired()])

class testResults(FlaskForm):
    test_name= StringField('Test Name',validators=[InputRequired()])
    artifact = StringField('Artifact')
