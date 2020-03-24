from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(150))
    orders = db.relationship('Order', back_populates='user')


class Meal(db.Model):
    __tablename__ = "meals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    price = db.Column(db.String(100))
    description = db.Column(db.String(300))
    picture = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey("categorys.id"))
    category = db.relationship('Category', back_populates='meals')


class Category(db.Model):
    __tablename__ ="categorys"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    meals = db.relationship('Meal', back_populates='category')


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(120))
    summary = db.Column(db.Integer)
    status = db.Column(db.String(30))
    meals_list = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship('User', back_populates='orders')