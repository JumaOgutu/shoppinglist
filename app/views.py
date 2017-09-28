import os    #allows for interface with the underlying OS that python is running
from flask import Flask, render_template, redirect, flash, url_for, request, session #modules are imported for ref purposes,includes functions, classes and variables
from app import app #app is the object imported from the app package that has the __init__ file
from app.models.users import Users #
from app.models.items import Items

import validators

app.secret_key = "thinktank!"

username=[] #an empty list that stores my usernames
email = []
password = []
created_users = {} #an empty dict that stores my created users
email = []
shoppinglist={}

#Function to create users
def create_user(username, email, password):#a function called create_user whose args are u,e,p and are passed when the function is called
   
    users = Users(username, email, password) #users is the instance of the class Users
    created_details = [email, password] #list that store email and password from client
    created_users[username] = created_details #key is username and the value are the email and password in created details
    return created_users#the function returns this and is stored in the dict



@app.route('/', methods=['GET', 'POST']) #route decorator binds my function "index" to a URL.
def index():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        word = request.form['password']
        
        if name in username:
            if word in password:
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
        if email not in email:
            if validators.email(email):
                if username not in username:
                    if len(password) > 5:                
                        if password == confirm_password:
                            create_user(username, email, password)
                            email.append(email)
                            username.append(username)
                            password.append(password)
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