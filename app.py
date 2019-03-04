from flask import Flask, render_template, request, session, url_for, redirect
import os
import sqlite3

DB_FILE = "data/database.db"
app = Flask(__name__)
app.secret_key=os.urandom(32)

db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pwd TEXT)")
db.commit()
db.close()

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['POST'])
def auth():
    givenUname=request.form["username"]
    givenPwd=request.form["password"]
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT CASE WHEN COUNT (name) >= 1 THEN CAST (1 AS BIT) ELSE CAST (0 AS BIT) END AS isItValid FROM users WHERE users.name = '" + givenUname + "' AND users.pwd = '" + givenPwd + "'")
    fetched = c.fetchall()
    print(fetched)
    for result in fetched:
        if result[0] == 1:
            return redirect(url_for('home'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
