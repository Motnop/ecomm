import random
from flask import render_template

from app import app, db
from models import User, Order, Meal, Category
from forms import *


@app.route('/')
def index():
    categorys = random.sample(db.session.query(Category).all(), 3)
    meals = db.session.query(Meal).all()
    return render_template('index.html', meals=meals, categorys=categorys)


@app.route('/cart/')
def cart():
    return render_template('cart.html')


@app.route('/account/')
def account():
    return render_template('account.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/logout/')
def logout():
    return render_template('login.html')


@app.route('/ordered/')
def ordered():
    return render_template('ordered.html')