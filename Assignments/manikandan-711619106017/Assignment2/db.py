import ibm_db
try:

 conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL;SSlServerCertificate=DigiCertGlobalRootCA.crt;UID=kbt24804;PWD=A5vX3tpOo0pdMKym;", '', '')
 print("db is connected")
except:
    print("db is not connected")