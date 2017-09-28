import os    #allows for interface with the underlying OS that python is running
from flask import Flask, render_template, redirect, flash, url_for, request, session #modules are imported for ref purposes,includes functions, classes and variables
from app import app #app is the object imported from the app package that has the __init__ file
from app.models.users import Users #import object of the users class
from app.models.shoppinglist import S_list, shopping_lists #import object of the s-list class
from app.models.items import Items #import object of the items class

import validators #to check if a given string is an email

app.secret_key = "thinktank!"

user_name=[] #an empty list that stores my usernames
e_mail = []
pass_word = []
created_users = {} #an empty dict that stores my created users
shoppinglist={}#dict that will store my shopping list
itemlist={}#dict that will store my item list

#Function to create users
def create_user(username, email, password, shoppinglist):#a function called create_user whose args are u,e,p and are passed when the function is called
   
    users = Users(username, email, password, shoppinglist) #users is the instance of the class Users
    created_details = [email, password] #list that store email and password from client
    created_users[username] = created_details #key is username and the value are the email and password in created details
    return created_users#the function returns this and is stored in the dict

def add_shoppinglist(title, items): #function that adds a new shopping list

    slist=S_list(title, items) #slist is the instance of the class S_list
    shopping_lists.append(slist)#adds a shopping list to others
    
    return True


@app.route('/', methods=['GET', 'POST']) #route decorator binds my function "index" to a URL
def index():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        word = request.form['password']

        
        if name in user_name:
            if word in pass_word:
                session['logged_in'] = True
                session['id'] = name
                return redirect('/')
            else:
                error = 'Enter correct password'
        else:
            error = 'Username does not exist'
    
    return render_template("index.html", error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']  #After you enter the username and password and click submit the route will be invoked again as a POST request and both request.form['username'] and request.form['password'] will be set to the values entered by the user.
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if email not in e_mail:
            if validators.email(email):
                if username not in user_name:
                    if len(password) > 5:                
                        if password == confirm_password:
                            create_user(username, email, password, shoppinglist)
                            e_mail.append(email)
                            user_name.append(username)
                            pass_word.append(password)
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
    
    