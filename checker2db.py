import os
from sqlite3 import Timestamp
import mysql.connector
import time
import subprocess
mysql_user=os.environ['DBUSER']
mysql_pass=os.environ['DBPASS']
mysql_host=os.environ['DBHOST']
mysql_db=os.environ['DBNAME']
mydb=mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_pass,
    database=mysql_db
)
mycursor=mydb.cursor()
ip_file = open('<path/to/list>', 'r')
for line in ip_file:
    response=subprocess.Popen(["ping", "-c", "1", line.strip().split(",")[0]],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    if (response.returncode == 0):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        hostid = line.strip().split(",")[1]
        ipaddr = line.strip().split(",")[0]
        state = "up"
    else:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        hostid = line.strip().split(",")[1]
        ipaddr = line.strip().split(",")[0]
        state = "down"
        pass
    sql = "INSERT INTO ping (timestamp, hostid, ipaddr, state) VALUES (%s, %s, %s, %s)"
    val = (timestamp, hostid, ipaddr, state)
    mycursor.execute(sql, val)
    mydb.commit()



