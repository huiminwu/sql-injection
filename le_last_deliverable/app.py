from flask import Flask, render_template, request, session, url_for, redirect, flash
import os
import sqlite3

DB_FILE = "data/database.db"
app = Flask(__name__)
app.secret_key=os.urandom(32)

db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, pwd TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS classified (file_name TEXT PRIMARY KEY, description TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS public_info (file_name TEXT PRIMARY KEY, description TEXT)")
db.commit()
db.close()

@app.route('/')
def index():
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
            flash("Congrats! You cracked the system!")
            return redirect(url_for('index'))
    flash("Try again!")
    return redirect(url_for('index'))

@app.route('/auth_2', methods = ['POST'])
def auth_2():
    givenSearch=request.form["search"]
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='public_info';")
    fetched = c.fetchall()

    c.execute("SELECT * from public_info WHERE file_name LIKE '" + givenSearch + "%'")
    fetched = c.fetchall()

    flash("Your search returned " + str(fetched))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
