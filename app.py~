from flask import Flask, render_template, request, session, url_for, redirect
import os
import sqlite3
DB_FILE = "database.db"
app = Flask(__name__)
app.secret_key=os.urandom(32)

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pwd TEXT)")

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
