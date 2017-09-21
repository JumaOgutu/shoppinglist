from flask import Flask, render_template, redirect, flash, url_for, request, session
from app import app
import os

# app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template("index.html")

@app.route('/register')
def register():
    
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    
    return render_template("dashboard.html")