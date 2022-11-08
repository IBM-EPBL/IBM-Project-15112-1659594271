
from flask import Flask,render_template,request,redirect
from flask_mail import  Mail, Message
from random import *  
import db
import os
from db import ibm_db
app = Flask(__name__)
mail = Mail(app)
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mani567459@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = randint(000000,999999)  
print(otp)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def home():
  return render_template("index.html")

@app.route('/index')
def homepage():
  return render_template("index.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    global userid
    mesg = ''
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    

    
        
        sql = "SELECT * FROM USERDETAILS WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(db.conn,sql)
        
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            return "Login Sucessfully"
        else:
            mesg = 'Invalid details. Please check the Email ID - Password combination.!'
            return render_template("index.html",mesg=mesg)
            





@app.route('/register', methods=['GET', 'POST'])
def register():
    global username
    global email
    global phone
    global password

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        msg = Message('OTP',sender = 'mani567459@gmail.com', recipients = [email])  
        msg.body = str(otp)
        
        phone = request.form['phone']
        password = request.form['password']
       
        sql = "SELECT * FROM USERDETAILS WHERE email = ?"
        stmt = ibm_db.prepare(db.conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
       
       
        if account:
            mesg='Job Recommender Account Already exist.kindly login!'
            return render_template("index.html",mesg=mesg)
        else:
            messg=mail.send(msg)  
            return render_template("verify.html",username=username,email=email,phone=phone,password=password) 

 

@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):
        
        sql ="INSERT INTO USERDETAILS(USERNAME,EMAIL,PHONE,PASSWORD) VALUES('{0}','{1}','{2}','{3}')"
        res = ibm_db.exec_immediate(db.conn,sql.format(username,email,phone,password))
        mesg = "Your Job Recommender account successfully registered!"
        msg = Message('Registered Sucessfully',sender = 'mani567459@gmail.com', recipients = [email])  
        msg.body = 'your Job Recommender account registered successfully\nLogin id:\nemail:'+email+'\npassword:'+password
        mail.send(msg)  
    
        return render_template("index.html",mesg=mesg)
    else:
       return render_template("Invalid otp.Email is not verified")
 
        
        



if(__name__=='__main__'):
     port = os.environ.get("PORT",5000)
     app.run(port=port,host='0.0.0.0',debug=True)



