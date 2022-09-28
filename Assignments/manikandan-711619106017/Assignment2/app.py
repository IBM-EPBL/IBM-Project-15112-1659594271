
from flask import Flask,render_template,request,redirect
import db
from db import ibm_db


app = Flask(__name__)


@app.route("/")
def log():
  return render_template("index.html")

@app.route("/log.html")
def home():
  return render_template("log.html")

@app.route("/login")
def reg():
  return render_template("log.html")


@app.route("/login",methods=['POST'])
def login():
   email =request.form.get('lemail')
   password=request.form.get('lpassword')
   sql = "SELECT * FROM REGISTRATION WHERE EMAIL = ? AND PASSWORD= ?"
   stmt = ibm_db.prepare(db.conn,sql)

   ibm_db.bind_param(stmt,1,email)
   ibm_db.bind_param(stmt,2,password)
   ibm_db.execute(stmt)
   account = ibm_db.fetch_assoc(stmt)

   if account:
    return render_template("home.html")
   else:
    return "IVALID EMAILID/PASSWORD"
   
   
@app.route("/index.html")
def homepage():
  return render_template("index.html")



@app.route("/receivedata",methods=['GET','POST'])
def receivedata():
  name =request.form.get('name')
  email =request.form.get('email')
  phone =request.form.get('phone')
  password=request.form.get('password')
  sql = "SELECT * FROM REGISTRATION WHERE EMAIL = ?"
  stmt = ibm_db.prepare(db.conn, sql)
  ibm_db.bind_param(stmt,1,email)
  ibm_db.execute(stmt)
  account = ibm_db.fetch_assoc(stmt)
  print(account)
  if account:
    return "Account Already exist"
  else:
    sql ="INSERT INTO REGISTRATION(NAME,EMAIL,PHONE,PASSWORD) VALUES('{0}','{1}','{2}','{3}')"
    res = ibm_db.exec_immediate(db.conn,sql.format(name,email,phone,password))
    if sql:
     return render_template("/login")
  
    
  
  
   



if(__name__=='__main__'):
    app.run(debug = True)