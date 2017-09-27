import os
from flask import Flask, render_template, redirect, flash, url_for, request, session
from app import app
from app.models.users import Users
import validators

app.secret_key = "thinktank!"

# app = Flask(__name__)

app.username=[]
app.email = []
app.password = []
app.created_users = {}

#Function to create users
def create_user(username, email, password):
    # app.created_users = {}
    created_users = Users(username, email, password)
    created_details = [email, password]
    app.created_users[username] = []
    app.created_users[username] = created_details
    return app.created_users

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        word = request.form['password']
        
        if name in app.username:
            if word in app.password:
                session['logged_in'] = True
                session['id'] = name
                return redirect('/')
            else:
                error = 'Enter correct password'
        else:
            error = 'Username does not exist'
    else:
        return render_template("index.html", error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if email not in app.email:
            if validators.email(email):
                if username not in app.username:
                    if len(password) > 5:                
                        if password == confirm_password:
                            create_user(username, email, password)
                            app.email.append(email)
                            app.username.append(username)
                            app.password.append(password)
                            return redirect('/')
                        else:
                            error = 'Enter matching passwords'
                    else:
                        error = 'Password should have more than 5 characters'
                else:
                    error = 'Username already exists'
            else:
                error = 'Enter a valid email'
        else:
            error = 'Email already exists'
    
    return render_template("register.html", error = error)

@app.route('/dashboard')
def dashboard():
    
    return render_template("dashboard.html")