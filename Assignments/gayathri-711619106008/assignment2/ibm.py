import ibm_db
try:

 conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSlServerCertificate=DigiCertGlobalRootCA (1).crt;UID=ndl78967;PWD=ThL40fdXxY7kP6us;", '', '')
 print("db is connected")
except:
    print("db is not connected")