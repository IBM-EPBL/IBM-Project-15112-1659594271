import ibm_db
try:
 conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSlServerCertificate= DigiCertGlobalRootCA (2).crt;PROTOCOL=TCPIP;UID=bww04013;PWD=gX5s1eXKFcXkHw2y;", "", "")
 print("db is connected")

except:
    print("db is not connected")