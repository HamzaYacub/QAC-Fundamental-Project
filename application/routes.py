from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/rent')
def rent():
    return render_template('rent.html', title="Rent a Car")

@app.route('/add_car')
def add_car():
    return render_template('addCar.html', title="Add a Car")

@app.route('/rental_history')
def rental_history():
    return render_template('rentalHistory.html', title="Rental History")

@app.route('/login')
def login():
    return render_template('login.html', title="Login")

@app.route('/register')
def register():
    return render_template('register.html', title="Register")
