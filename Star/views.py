from Star import app
from flask import render_template, request, abort, session, flash, redirect, url_for
from Star import users as mdb, user, util

import json

david = user.User('David Bundgaard', 'dbundgaard', 'dapoman@gmail.com')


# manual encoding
def encode_user(user):
    return {"_type": "user", "name": user.name(), "username": user.username, "email": user.email}


def decode_user(user_document):
    assert user_document['_type'] == 'user'
    return user.User(user_document['name'], user_document['username'], user_document['email'])


@app.route("/")
def home():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    # result = mdb.db.users.insert({'user': encode_user(david)})
    return render_template('app/index.html', username=session['username'])


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        if request.form['x-username'] != 'username' or request.form['x-password'] != 'password':
            flash("Wrong username and/or password.")
            return redirect(url_for('login'))
        else:
            session['logged_in'] = True
            session['username'] = request.form['x-username']
            flash('Successful login')
            return redirect(url_for('home'))
    return render_template('app/login.html')


@app.route('/logout')
def logout():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    session.pop('logged_in')
    return render_template('app/logout.html')

@app.route("/knockout")
def knockout():
    return render_template('app/list_knockout.html')