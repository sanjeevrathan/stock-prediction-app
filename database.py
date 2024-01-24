import mysql.connector
conn = mysql.connector.connect(host='localhost', password='', user='root', database='test', port = 3306)

if conn.is_connected():
    print("Connection established")

cursor = conn.cursor()
cur = conn.cursor()
#cursor.execute("select email from loginpy")
sql = 'select username from loginpy'
cursor.execute(sql)
s = cursor.fetchall()
sql1 = 'select email from loginpy'
cur.execute(sql1)
r = cur.fetchall()
for i in s:
    print(i)
for j in r:
    print(j)
