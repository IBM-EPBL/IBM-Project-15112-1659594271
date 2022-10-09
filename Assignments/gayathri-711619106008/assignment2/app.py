from flask import Flask,render_template,request,redirect
import ibm
from ibm import ibm_db


app = Flask(__name__)


@app.route("/")
def login():
  return render_template("login.html")


@app.route("/login.html")
def reg():
  return render_template("login.html")

@app.route("/register form.html")
def register():
    return render_template("register form.html")

@app.route("/log",methods=['POST'])
def log():
   email =request.form.get('email')
   password=request.form.get('password')
   sql = "SELECT * FROM USERDETAILS WHERE EMAIL = ? AND PASSWORD= ?"
   stmt = ibm_db.prepare(ibm.conn,sql)

   ibm_db.bind_param(stmt,1,email)
   ibm_db.bind_param(stmt,2,password)
   ibm_db.execute(stmt)
   account = ibm_db.fetch_assoc(stmt)

   if account:
    return render_template("sucess.html")
   else:
    return "INVALID EMAILID/PASSWORD"




@app.route("/register",methods=['GET','POST'])
def receivedata():
  name =request.form.get('name')
  email =request.form.get('email')
  password=request.form.get('password')
  roll =request.form.get('roll')
  sql = "SELECT * FROM USERDETAILS WHERE EMAIL = ?"
  stmt = ibm_db.prepare(ibm.conn, sql)
  ibm_db.bind_param(stmt,1,email)
  ibm_db.execute(stmt)
  account = ibm_db.fetch_assoc(stmt)
  print(account)
  if account:
    return "Account Already exist"
  else:
    sql ="INSERT INTO USERDETAILS(NAME,EMAIL,PASSWORD,ROLLNUMBER) VALUES('{0}','{1}','{2}','{3}')"
    res = ibm_db.exec_immediate(ibm.conn,sql.format(name,email,password,roll))
    if sql:
     return render_template("/login.html")












if(__name__=='__main__'):
    app.run(debug = True)