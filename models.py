from app import db, login_manager
from flask_login import UserMixin

# Customer table
class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    tintas = db.relationship('Tinta', passive_deletes=True, backref='customer', lazy=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<Name %r>' % self.name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone
       }

# Tinta table
class Tinta(db.Model):
    __tablename__ = 'tinta'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    description = db.Column(db.String(100))
    date = db.Column(db.String(40))
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id', ondelete='CASCADE'),
        nullable=False)

    def __init__(self, description, date, customerId):
        self.description = description
        self.date = date
        self.customerId = customerId


# User table
class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
