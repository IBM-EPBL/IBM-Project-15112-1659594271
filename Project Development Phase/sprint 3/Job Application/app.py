
from flask import Flask,render_template,request,redirect,session
from flask_mail import  Mail, Message
from flask import render_template_string

import csv
import m
import uuid
import json
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
app.config['MAIL_PASSWORD'] = 'olnlgwvxsxmchrps'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = randint(000000,999999)  
print(otp)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def welcome():
  global row
  return render_template("index.html")



@app.route('/detail')
def detail():
   
      if db.conn:
          sql="SELECT * FROM EMPLOYER"
          smt= ibm_db.exec_immediate(db.conn,sql)
          res = ibm_db.fetch_both(smt)
          result=[]
          while res != False:
            result.append(res)
            row=len(result) 
            res = ibm_db.fetch_both(smt)
          return render_template("del.html",r=result,rows=row)

@app.route('/index')
def homepage():
  return render_template("index.html")

@app.route('/admin2')
def admin2():
  return render_template("admin.html")

@app.route('/employer.html')
def employer():
   return render_template("employer.html")




@app.route('/home.html')
def postjob():
             sql = "SELECT * FROM USERDETAILS WHERE ID='{0}' "
             smt = ibm_db.prepare(db.conn, sql.format(session["UID"]))
             ibm_db.execute(smt)
             res=ibm_db.fetch_assoc(smt)
             return render_template("home.html",data=res)




@app.route('/login', methods = ['GET', 'POST'])
def login():
    global userid
    global email
    
    mesg = ''
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
    

    
        
        sql = "SELECT * FROM USERDETAILS WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(db.conn,sql)
        
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        res = ibm_db.fetch_assoc(stmt)
        print(res)
        if res:
            session["UID"]=res['ID']
            return render_template("home.html",data=res)
        else:
            mesg = 'Invalid details. Please check the Email ID - Password combination.!'
            return render_template("index.html",mesg=mesg)


@app.route('/login1', methods = ['GET', 'POST'])
def login1():
    global userid
    
    
    mesg = ''
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
    

    
        
        sql = "SELECT * FROM EMPLOYER WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(db.conn,sql)
        
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        res = ibm_db.fetch_assoc(stmt)
        print(res)
        if res:
            session["UID"]=res['ID']
            return render_template("job.html")
        else:
            mesg = 'Invalid details. Please check the Email ID - Password combination.!'
            return render_template("employer.html",mesg=mesg)


@app.route('/register1', methods=['GET', 'POST'])
def register1():
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
       
        sql = "SELECT * FROM EMPLOYER WHERE email = ?"
        stmt = ibm_db.prepare(db.conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
       
       
        if account:
            mesg='Job Recommender Employer Account Already exist.kindly login!'
            return render_template("employer.html",mesg=mesg)
        else:
            messg=mail.send(msg)  
            return render_template("verify1.html",username=username,email=email,phone=phone,password=password,data=account) 




@app.route('/admin1', methods = ['GET', 'POST'])
def adminlogin():
    global userid
   
    
    mesg = ''
    
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        
    

    
        
        sql = "SELECT * FROM ADMIN WHERE username = ? AND password = ?"
        stmt = ibm_db.prepare(db.conn,sql)
        
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        res = ibm_db.fetch_assoc(stmt)
        print(res)
        if res:
            return redirect('/admin')
        else:
            mesg = 'Invalid details. Please check the USERNAME - Password combination.!'
            return render_template("admin.html",mesg=mesg)
            


@app.route("/job", methods=['POST', 'GET'])
def job():
           
  if request.method == 'POST':

     id = request.form['job']
     company = request.form['cname']
     role = request.form['role']
     ex = request.form['ex']
     skill = request.form['skill']
     vacancy = request.form['vacancy']
     stream = request.form['stream']
     location = request.form['location']
     salary = request.form['salary']
     website= request.form['website']
     logo= request.form['logo']
     d= request.form['d']
     e= request.form['e']
     f= request.form['f']
     
     m.home(id,company,role,ex,skill,vacancy,stream,location,salary,website,logo,d,e,f)
     return render_template("home.html",data='Job Recommender')


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
            return render_template("verify.html",username=username,email=email,phone=phone,password=password,data=account) 

 

@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):
        
        sql ="INSERT INTO USERDETAILS(ID,USERNAME,EMAIL,PHONE,PASSWORD) VALUES('{0}','{1}','{2}','{3}',{4})"
        res = ibm_db.exec_immediate(db.conn,sql.format(uuid.uuid4(),username,email,phone,password))
        mesg = "Your Job Recommender account successfully registered!"
        msg = Message('Registered Sucessfully',sender = 'mani567459@gmail.com', recipients = [email])  
        msg.body = 'your Job Recommender account registered successfully\nLogin id:\nemail:'+email+'\npassword:'+password
        mail.send(msg)  
    
        return render_template("index.html",mesg=mesg)
    else:
        mesg ="Invalid otp.Kindly Enter the valid otp!"
        return render_template("verify.html",mesg=mesg)


@app.route('/validate1',methods=["POST"])  
def validate1():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):
        
        sql ="INSERT INTO EMPLOYER(USERNAME,EMAIL,PHONE,PASSWORD) VALUES('{0}','{1}','{2}','{3}')"
        res = ibm_db.exec_immediate(db.conn,sql.format(username,email,phone,password))
        mesg = "Your Job Recommender EMPLOYER account successfully registered!"
        msg = Message('Registered Sucessfully',sender = 'mani567459@gmail.com', recipients = [email])  
        msg.body = 'your Job Recommender EMPLOYER account registered successfully\nLogin id:\nemail:'+email+'\npassword:'+password
        mail.send(msg)  
    
        return render_template("employer.html",mesg=mesg)
    else:
        mesg ="Invalid otp.Kindly Enter the valid otp!"
        return render_template("verify1.html",mesg=mesg)
 
 
        
@app.route("/home", methods=['POST', 'GET'])
def home():
        if "UID" in session:

            if request.method == 'POST':
             sql = "SELECT * FROM USERDETAILS WHERE ID='{0}' "
             smt = ibm_db.prepare(db.conn, sql.format(session["UID"]))
             ibm_db.execute(smt)
             res=ibm_db.fetch_assoc(smt)
             user_search = request.form.get('search')
             arr = []
             with open("data.csv", 'r') as file:
                 csvreader = csv.reader(file)
                 for i in csvreader:
                     if i[2].casefold() == user_search.casefold():
                         dict = {
                             'jobid': i[0], 'cname': i[1], 'role': i[2], 'ex': i[3], 'skill': i[4], 'vacancy': i[5], 'stream': i[6], 'job_location': i[7], 'salary': i[8], 'link': i[9], 'logo': i[10],'d':i[11],'e':i[12],'f':i[13]
                         }
                         arr.append(dict)
             companies = json.dumps(arr)

             return render_template("home.html", companies=companies, arr=arr,data=res)
            else:
             sql = "SELECT * FROM USERDETAILS WHERE ID='{0}' "
             smt = ibm_db.prepare(db.conn, sql.format(session["UID"]))
             ibm_db.execute(smt)
             res=ibm_db.fetch_assoc(smt)
             user_search = 'Web developer'
             arr = []
             with open("data.csv", 'r') as file:
                 csvreader = csv.reader(file)
                 for i in csvreader:
                     if i[2].casefold() == user_search.casefold():
                         dict = {
                             'jobid': i[0], 'cname': i[1], 'role': i[2], 'ex': i[3], 'skill': i[4], 'vacancy': i[5], 'stream': i[6], 'job_location': i[7], 'salary': i[8], 'link': i[9], 'logo': i[10]
                         }
                         arr.append(dict)
             companies = json.dumps(arr)

             return render_template("home.html", companies=companies, arr=arr,data=res)
        else:
         return render_template("index.html")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        fields = json.loads(request.args.get('fields').replace("'", '"'))
        
        return render_template_string('''
           <html>
             <head>
               <!-- Bootstrap CDN -->
               <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"/>
             </head>
             <body>
               <div class="container mt-5 text-center">
                 <h3>Post new Job:</h3>
                 <form class="mt-4" method="POST">
                   {% for field in fields %}
                     <div class="col mt-2">
                       <div class="row mx-auto" style="width: 300px">
                         <input name="{{field}}" type="text" class="form-control" placeholder="{{field}}">
                       </div>
                     </div>
                   {% endfor %}
                   
                   <!-- Submit form button -->
                   <input type="submit" class="btn btn-success mt-4" value="Submit"/>
                 </form>
               </div>
             </body>
           </html>
        ''', fields=fields)
    
    elif request.method == 'POST':
        data = dict(request.form)
        
        with open('data.csv', 'a',newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writerow(data)
        
        return redirect('/admin')

@app.route('/admin')
def read():
    data = []
    
    with open('data.csv') as f:
        reader = csv.DictReader(f)
        
        [data.append(dict(row)) for row in reader]
    
    return render_template_string('''
       <html>
         <head>
           <!-- Bootstrap CDN -->
           <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"/>
            <style>
  button{
  width: 130px;
  background-color: #5995fd;
  border: none;
  outline: none;
  height: 49px;
  border-radius: 49px;
  color: #fff;
  text-transform: uppercase;
  font-weight: 600;
  margin: 10px 0;
  cursor: pointer;
  transition: 0.5s;
  padding-left:48;
  margin-left:1000px;
  padding-right:50px;
  }

  button:hover{
  background-color: #4d84e2;
}
    </style>
         </head>
         <body>
           <div class="container">
             <!-- CRUD operations -->
             <div class="col">
               
               <!--a class="btn btn-danger mt-5" href="/create">Delete</a-->
             </div>
             
             <!-- CSV data -->
             <table class="table table-striped mt-2" style="width: 100%; border: 1px solid black">
               <thead>
                 <tr class="bg-secondary text-white">
                   {% for header in data[0].keys() %}
                     <th scope="col">
                       {% if header == list(data[0].keys())[0] %}
                         <a class="btn btn-outline-light" href="/create?fields={{str(list(data[0].keys()))}}" style="margin-right: 5px;">+</a>
                       {% endif%}
                       {{ header}}
                     </th>
                   {% endfor %}
                 </tr>
               </thead>
               <tbody>
                 {% for row in range(0, len(data)) %}
                   <tr id="{{row}}">
                     {% for col in range(0, len(list(data[row].values()))) %}
                       <td style="word-break:break-all;">
                         {% if col == 0 %}
                           <a class="btn btn-outline-danger" href="/delete?id={{row}}" style="margin-right: 5px;">x</a>
                           <a href="/update?id={{row}}">{{ list(data[row].values())[col] }}</a>
                         {% else %}
                           {{ list(data[row].values())[col] }}
                         {% endif %}
                     {% endfor %}
                 {% endfor%}
               </tbody>
             </table>
           </div>
            <form action="/home.html">
       <button type="submit">Back</button>
    </form> 
     <form action="/detail">
       <button type="submit">NEXT</button>
    </form>
         </body>
       </html>
    ''', data=data, list=list, len=len, str=str)



@app.route('/delete')
def delete():
   
    with open('data.csv') as rf:
       
        data = []
        
       
        temp_data = []
        
       
        reader = csv.DictReader(rf)
        
       
        [temp_data.append(dict(row)) for row in reader]
        
       
        [
            data.append(temp_data[row]) 
            for row in range(0, len(temp_data))
            if row != int(request.args.get('id'))
        ]

      
        with open('data.csv', 'w',newline='') as wf:
           
            writer = csv.DictWriter(wf, fieldnames=data[0].keys())
            
          
            writer.writeheader()
            
            
            writer.writerows(data)

    
    return redirect('/admin')



@app.route('/logout')
def logout():
        session.pop("UID",None)
        return redirect("/index")


@app.route("/dele/<string:id>",methods=['POST','GET'])
def dele(id):
         sql="DELETE FROM EMPLOYER WHERE id='{0}'"
         smt=ibm_db.exec_immediate(db.conn,sql.format(id))
         return redirect("/detail")



        

if(__name__=='__main__'):
     port = os.environ.get("PORT",5000)
     app.run(port=port,host='0.0.0.0',debug=True)



