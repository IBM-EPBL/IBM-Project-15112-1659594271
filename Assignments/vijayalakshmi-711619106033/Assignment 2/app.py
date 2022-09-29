from flask import Flask,render_template,request,redirect
import main
from main import ibm_db


app = Flask(__name__)


@app.route("/")
def log():
  return render_template("login.html")

@app.route("/login.html")
def signin():
  return render_template("login.html")

@app.route("/login",methods=['POST'])
def login():
   email =request.form.get('email')
   password=request.form.get('password')
   sql = "SELECT * FROM REG WHERE EMAIL = ? AND PASSWORD= ?"
   stmt = ibm_db.prepare(main.conn,sql)

   ibm_db.bind_param(stmt,1,email)
   ibm_db.bind_param(stmt,2,password)
   ibm_db.execute(stmt)
   account = ibm_db.fetch_assoc(stmt)

   if account:
    return "LOGIN SUCESSFULLY"
   else:
    return "INVALID EMAILID/PASSWORD"


@app.route("/signup.html")
def homepage():
  return render_template("signup.html")



@app.route("/register",methods=['GET','POST'])
def register():
  name =request.form.get('name')
  email =request.form.get('email')
  roll =request.form.get('roll')
  password=request.form.get('password')
  sql = "SELECT * FROM REG WHERE EMAIL = ?"
  stmt = ibm_db.prepare(main.conn, sql)
  ibm_db.bind_param(stmt,1,email)
  ibm_db.execute(stmt)
  account = ibm_db.fetch_assoc(stmt)
  print(account)
  if account:
    return "Account Already exist"
  else:
    sql ="INSERT INTO REG(NAME,EMAIL,ROLLNUMBER,PASSWORD) VALUES('{0}','{1}','{2}','{3}')"
    res = ibm_db.exec_immediate(main.conn,sql.format(name,email,roll,password))
    if sql:
     return render_template("login.html")
  












if(__name__=='__main__'):
    app.run(debug = True)
