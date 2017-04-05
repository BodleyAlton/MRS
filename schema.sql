create database med_records;
use med_records;

create table test_result(
  test_name varchar(60),
  tr_id int,
  artifact varchar(60),
  primary key (tr_id)
);

create table treatment(
  t_id int,
  treatment_name varchar(60),
  primary key (t_id)
);

create table cprocedure(
  pro_id int,
  pro_name varchar(60),
  primary key (pro_id)
);

create table diagnosis(
  d_id int,
  d_name varchar(60),
  primary key (d_id)
);

create table vitals(
  vitals_id int(1),
  vital_sign varchar(30),
  primary key(vitals_id)
);

create table disease(
  code varchar(10),
  disease_name varchar(20),
  primary key(code)
);

create table meds(
  m_id varchar(10),
  m_name varchar(20),
  primary key(m_id)
);

create table nurse(
  ncontact varchar(14),
  n_eid int(7),
  nf_name varchar(15),
  nl_name varchar(15),
  address_1 varchar(20),
  address_2 varchar(20),
  city varchar(20),
  parish varchar(20),
  primary key(n_eid)
);

create table registered_midwife(
  n_eid int(7),
  type varchar(10),
  primary key (n_eid, type),
  foreign key (n_eid) references nurse(n_eid) on delete cascade on update cascade
);

create table registered(
  n_eid int(7),
  type varchar(10),
  primary key (n_eid, type),
  foreign key (n_eid) references nurse(n_eid) on delete cascade on update cascade
);

create table enrolled(
  n_eid int(7),
  type varchar(10),
  primary key (n_eid, type),
  foreign key (n_eid) references nurse(n_eid) on delete cascade on update cascade
);

create table doctor(
  d_eid int(7),
  df_name varchar(15),
  dl_name varchar(15),
  dcontact varchar(14),
  address_1 varchar(20),
  address_2 varchar(20),
  city varchar(20),
  parish varchar(20),
  primary key(d_eid)
);

create table residents(
  d_eid int(7),
  type varchar(10),
  level varchar(5),
  primary key(d_eid, type),
  foreign key (d_eid) references doctor(d_eid) on delete cascade on update cascade
);

create table intern(
  d_eid int(7),
  dept varchar(10),
  type varchar(10),
  primary key(d_eid, dept),
  foreign key (d_eid) references doctor(d_eid) on delete cascade on update cascade
);

create table consultant(
  d_eid int(7),
  spec varchar(10),
  primary key(d_eid, spec),
  foreign key (d_eid) references doctor(d_eid) on delete cascade on update cascade
);

create table patient(
  p_trn int(9),
  pf_name varchar(15),
  pl_name varchar(15),
  dob date,
  address_1 varchar(20),
  address_2 varchar(20),
  city varchar(20),
  parish varchar(20),
  pcontact varchar(14),
  status varchar(10),
  primary key(p_trn)
);

create table family(
  relation varchar(6),
  d_id int,
  f_name varchar(15),
  l_name varchar(15),
  p_trn int(9),
  primary key(f_name, l_name, p_trn),
  foreign key(p_trn) references patient(p_trn) on delete cascade on update cascade,
  foreign key(d_id) references diagnosis(d_id) on delete cascade on update cascade
);

create table cupdate(
  m_id varchar(10),
  date_ date,
  vitals_id int(1),
  n_eid int(7),
  p_trn int(9),
  d_eid int(7),
  reading varchar(4),
  primary key(m_id,vitals_id,n_eid,p_trn,d_eid),
  foreign key(m_id) references meds(m_id) on delete cascade on update cascade,
  foreign key(vitals_id) references vitals(vitals_id) on delete cascade on update cascade,
  foreign key(n_eid) references nurse(n_eid) on delete cascade on update cascade,
  foreign key(p_trn) references patient(p_trn) on delete cascade on update cascade,
  foreign key(d_eid) references doctor(d_eid) on delete cascade on update cascade
);

create table alergy(
  id int,
  name varchar(10),
  severity varchar(50),
  m_id varchar(10),
  p_trn int(9),
  primary key (id),
  foreign key(m_id) references meds(m_id) on delete cascade on update cascade,
  foreign key(p_trn) references patient(p_trn) on delete cascade on update cascade
);

create table patient_history(
  code varchar(10),
  p_trn int(9),
  d_id int,
  pro_id int,
  t_id int,
  tr_id int,
  d_eid int (7),
  date_ date,
  primary key(code,p_trn,d_id,pro_id,t_id,tr_id),
  foreign key(code) references disease(code) on delete cascade on update cascade,
  foreign key(p_trn) references patient(p_trn) on delete cascade on update cascade,
  foreign key(d_id) references diagnosis(d_id) on delete cascade on update cascade,
  foreign key(pro_id) references cprocedure(pro_id) on delete cascade on update cascade,
  foreign key(t_id) references treatment(t_id) on delete cascade on update cascade,
  foreign key(tr_id) references test_result(tr_id) on delete cascade on update cascade,
  foreign key(d_eid) references doctor(d_eid) on delete cascade on update cascade
);
