import subprocess
from flask import Flask, render_template, request, session
import mysql.connector


def sql_connector():
  conn = mysql.connector.connect(user='root',password='',host='localhost',database ='test',port = 3306)
  c = conn.cursor()
  return conn, c


app = Flask(__name__)

@app.route('/login/', methods=['POST'])
def home():
    email = request.form['email']
    password = request.form['logpass']
    conn, c = sql_connector()
    c.execute("SELECT * FROM loginpy WHERE email =%s AND password =%s", (email,password))
    user = c.fetchone()
    c.close()
    
    if email is not None and password == email['logpass']:
      session['email'] = email['logpass']
      return render_template('login.html')
    else:
      error = 'Invalid username or password'
      return render_template('login.html', error=error)
    
@app.route('/register/', methods=['GET','POST'])
def home1():
  if request.method == 'POST':
    username = request.form.get('username')
    email = request.form.get('email')
    logpass = request.form.get('logpass')
    conn, c = sql_connector()
    c.execute("INSERT INTO loginpy (username, email, password) VALUES (%s, %s, %s)", (username, email, logpass))
    conn.commit()
    conn.close()
    c.close()
  return render_template("register.html")


@app.route('/')
def town():
  return render_template('login.html')

@app.route('/sanjeev/')
def my_link():
  return subprocess.run(["python", "san.py"])


if __name__ == "__main__":
    app.run(debug=True)