import mysql.connector

conn=mysql.connector.connect(host='localhost',password='Sujoy@2212',user='root',database='voter')
cur=conn.cursor()
s='SELECT * FROM voters'
cur.execute(s)
res=cur.fetchall()
for i in res:
    print(i)