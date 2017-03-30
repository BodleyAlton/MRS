from . import db
from flask.ext.login import UserMixin

class Nursedb(db.Model):
	__tablename__ = 'nurse'
	n_eid= db.Column('n_eid', db.Integer, primary_key= True)
	nf_name= db.Column('nf_name', db.Unicode)
	nl_name= db.Column('nl_name', db.Unicode)
	ncontact= db.Column('ncontact',db.Integer)
	address_1= db.Column('address_1', db.Unicode)
	address_2= db.Column('address_2', db.Unicode)
	city= db.Column('city', db.Unicode)
	parish= db.Column('parish', db.Unicode)

	def __init__(self,n_eid,nf_name,nl_name,ncontact,address_1,address_2,city,parish):
		self.n_eid= n_eid
		self.nf_name= nf_name
		self.nl_name= nl_name
		self.ncontact=ncontact
		self.address_1=address_1
		self.address_2=address_2
		self.city =city
		self.parish=parish

class Doctordb(db.Model):
    __tablename__ = 'doctor'
    d_eid= db.Column('d_eid', db.Integer, primary_key= True)
    df_name= db.Column('df_name', db.Unicode)
    dl_name= db.Column('dl_name', db.Unicode)
    dcontact= db.Column('dcontact',db.Integer)
    address_1= db.Column('address_1', db.Unicode)
    address_2= db.Column('address_2', db.Unicode)
    city= db.Column('city', db.Unicode)
    parish= db.Column('parish', db.Unicode)

    def __init__(self,d_eid,df_name,dl_name,dcontact,address_1,address_2,city,parish):
    	self.d_eid= d_eid
    	self.df_name= df_name
    	self.dl_name= dl_name
    	self.dcontact=dcontact
    	self.address_1=address_1
    	self.address_2=address_2
    	self.city =city
    	self.parish=parish

class Patientdb(db.Model):
    __tablename__='patient'
    p_trn= db.Column('p_trn', db.Integer, primary_key= True)
    pf_name= db.Column('pf_name', db.Unicode)
    pl_name= db.Column('pl_name', db.Unicode)
    dob= db.Column('dob', db.Unicode)
    address_1= db.Column('address_1', db.Unicode)
    address_2= db.Column('address_2', db.Unicode)
    city= db.Column('city', db.Unicode)
    parish= db.Column('parish', db.Unicode)
    pcontact= db.Column('pcontact', db.Unicode)

    def __inti__(self,p_trn,pf_name,pl_name,dob,address_1,address_2,city,parish,pcontact):
        self.p_trn = p_trn
        self.pf_name = pf_name
        self.pl_name = pl_name
        self.dob = dob
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.parish = parish
        self.pcontact = pcontact

class TestResults(db.Model):
    __tablename__='test_results'
    tr_id= db.Column('tr_id', db.Integer, primary_key= True)
    test_name= db.Column('test_name', db.Unicode)
    artifact= db.Column('artifact', db.Unicode)

    def __init__(self,tr_id,treatment_name):
        self.tr_id = tr_id
        self.treatment_name = treatment_name
        self.artifact = artifact

class Treatment(db.Model):
    __tablename__='treatment'
    t_id= db.Column('t_id', db.Integer, primary_key= True)
    treatment_name= db.Column('treatment_name', db.Unicode)

    def __init__(self,t_id,treatment_name):
        self.t_id = t_id
        self.treatment_name = treatment_name

class CProcudur(db.Model):
    __tablename__='cprocedure'
    pro_id= db.Column('pro_id', db.Integer, primary_key= True)
    pro_name= db.Column('pro_name', db.Unicode)

    def __init__(self, pro_id,pro_name):
        self.pro_id= pro_id
        self.pro_name = pro_name

class Diagnosis(db.Model):
    __tablename__='diagnosis'
    d_id= db.Column('d_id', db.Integer, primary_key= True)
    d_name= db.Column('d_name', db.Unicode)

    def __init__(self, d_id,d_name):
        self.d_id= d_id
        self.d_name = d_name

class Vitals(db.Model):
    __tablename__='vitals'
    vitals_id= db.Column('vitals_id', db.Integer, primary_key= True)
    vitals_sign= db.Column('vitals_sign', db.Unicode)

    def __init__(self, vitals_id,vitals_sign):
        self.vitals_id= vitals_id
        self.vitals_sign = vitals_sign

class Disease(db.Model):
    __tablename__='disease'
    code= db.Column('code', db.Unicode, primary_key= True)
    disease_name= db.Column('disease_name', db.Unicode)

    def __init__(self, vitals_id,vitals_sign):
        self.code= code
        self.disease_name = disease_name

class Meds(db.Model):
    __tablename__='meds'
    m_id= db.Column('m_id', db.Unicode, primary_key= True)
    m_name= db.Column('m_name', db.Unicode)

    def __init__(self, vitals_id,vitals_sign):
        self.m_id= m_id
        self.m_name = m_name

class RegisteredMidwife(db.Model):
    __tablename__='registered_midwife'
    n_eid= db.Column('n_eid', db.Unicode, primary_key= True)
    type_= db.Column('type', db.Unicode)

    def __init__(self, n_eid,type_):
        self.n_eid= n_eid
        self.type = type_

class Registered(db.Model):
    __tablename__='registered'
    n_eid= db.Column('n_eid', db.Unicode, primary_key= True)
    type_= db.Column('type', db.Unicode)

    def __init__(self, n_eid,type_):
        self.n_eid= n_eid
        self.type = type_

class Enrolled(db.Model):
    __tablename__='enrolled'
    n_eid= db.Column('n_eid', db.Unicode, primary_key= True)
    type_= db.Column('type', db.Unicode)

    def __init__(self, n_eid,type_):
        self.n_eid= n_eid
        self.type = type_

class Residents(db.Model):
    __tablename__='residents'
    d_eid= db.Column('n_eid', db.Unicode, primary_key= True)
    type_= db.Column('type', db.Unicode)
    level= db.Column('level', db.Unicode)

    def __init__(self, n_eid,type_,level):
        self.n_eid= n_eid
        self.type = type_
        self.level = level

class intern(db.Model):
    __tablename__='intern'
    d_eid= db.Column('d_eid', db.Unicode, primary_key= True)
    dept= db.Column('dept', db.Unicode)

    def __init__(self, n_eid,type_):
        self.d_eid= d_eid
        self.dept = dept

class Consultant(db.Model):
    __tablename__='Consultant'
    d_eid= db.Column('d_eid', db.Unicode, primary_key= True)
    spec= db.Column('spec', db.Unicode)

    def __init__(self, n_eid,type_):
        self.d_eid= d_eid
        self.spec = spec

class Family(db.Model):
    __tablename__='family'
    p_trn= db.Column('p_trn', db.Integer, primary_key= True)
    f_name= db.Column('f_name', db.Unicode, primary_key=True)
    l_name= db.Column('l_name', db.Unicode, primary_key=True)
    relation= db.Column('relation', db.Unicode)
    d_id= db.Column('d_id', db.Unicode)

    def __inti__(self,p_trn,f_name,l_name,relation,d_id):
        self.p_trn = p_trn
        self.f_name = f_name
        self.l_name = l_name
        self.relation = relation
        self.d_id = d_id

class Cupdate(db.Model):
    __tablename__='cupdate'
    m_id= db.Column('m_id', db.Integer, primary_key= True)
    date= db.Column('date', db.Unicode)
    vitals_id= db.Column('vitals_id', db.Integer, primary_key= True)
    n_eid= db.Column('n_eid', db.Integer, primary_key= True)
    p_trn= db.Column('p_trn', db.Integer, primary_key= True)
    d_eid= db.Column('d_eid', db.Integer, primary_key= True)

    def __inti__(self,m_id,date,vitals_id,n_eid,p_trn,d_eid):
        self.m_id = m_id
        self.date = date
        self.vitals_id = vitals_id
        self.n_eid = relation
        self.p_trn = p_trn
        self.d_eid = d_eid

class Alergy(db.Model):
        __tablename__='alergy'
        id= db.Column('m_id', db.Integer, primary_key= True)
        name= db.Column('date', db.Unicode)
        sevecrity= db.Column('vitals_id', db.Integer)
        m_id= db.Column('n_eid', db.Integer)
        p_trn= db.Column('p_trn', db.Integer)

        def __inti__(self,id,name,sevecrity,m_id,p_trn):
            self.id = id
            self.name = name
            self.sevecrity = sevecrity
            self.m_id = m_id
            self.p_trn = p_trn

class PatientHistory(db.Model):
    __tablename__='patient_history'
    code= db.Column('code', db.Integer, primary_key= True)
    pro_id= db.Column('pro_id', db.Unicode)
    d_id= db.Column('d_id', db.Integer)
    t_id= db.Column('t_id', db.Integer)
    p_trn= db.Column('p_trn', db.Integer)
    tr_id= db.Column('tr_id', db.Integer)


    def __inti__(self,code,pro_id,d_id,t_id,p_trn,tr_id):
        self.code = code
        self.pro_id = pro_id
        self.d_id = d_id
        self.t_id = t_id
        self.p_trn = p_trn
        self.tr_id = tr_id
