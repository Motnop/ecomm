import random
from flask import render_template
from flask import session
from flask import redirect, url_for


from app import app, db
from models import User, Order, Meal, Category
from forms import *

def info_cart():
    summary = 0
    cart = session.get("cart", {})
    meals = db.session.query(Meal).filter(Meal.id.in_(cart))
    for meal in meals:
        summary += int(meal.price)*cart[meal.id]
    return {"summary": summary, "count": len(cart)}

@app.route('/')
def index():
    meals = db.session.query(Meal).all()
    categorys = random.sample(db.session.query(Category).all(), 3)
    return render_template('index.html', meals=meals, categorys=categorys, info_cart=info_cart())



@app.route('/add/<meal>/')
def add(meal):
    cart = session.get("cart", {} )
    for row in cart:
        if row["meal_id"] == meal:
           row["count"] += 1
    else:
        cart.append({"meal_id" : meal, "count" : 1})

    session['cart'] = cart
    return redirect(url_for('cart_page'))


@app.route('/cart/')
def cart_page():
    cart = info_cart()
    meals = db.session.query(Meal).filter(Meal.id.in_(cart))
    return render_template('cart.html', meals=meals, cart=cart, info_cart=info_cart())


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