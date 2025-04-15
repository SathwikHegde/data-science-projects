import cx_Oracle

# conn =cx_oracle.connet('username/password@ipaddress or hostname/SID')
con=cx_Oracle.connect('INTBZ/intbz12#$@206.245.13.25/HRBOTEST')
ver=con.version.split(" . ")
#print(ver)
# instantiate a cursor obj
cur=con.cursor()
cur.execute("select * from pa0000_src")
row = cur.fetchone()
#row=cur.fetchmany(no.of.rec)
print (row)
#ctypes.windll.user32.MessageBoxW(0, "               " + str(row), "Result", 1)
cur.close()
con.close()
