from application import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey

class Cars(db.Model):
    __tablename__ = 'cars'
    car_ID = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20))
    year = db.Column(db.Date, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    gearbox = db.Column(db.String(20))
    doors = db.Column(db.Integer())
    seats = db.Column(db.Integer())
    fuel_type = db.Column(db.String(20))
    engine_size = db.Column(db.Integer())
    colour = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    rentals = db.relationship('Rentals', backref='car', lazy=True)

    def __repr__(self):
        return ''.join([
            'Car: ', str(self.car_ID)
            ])

class Rentals(db.Model):
    __tablename__ = 'rentals'
    rental_ID = db.Column(db.Integer, primary_key=True)
    car_ID = db.Column(db.Integer, db.ForeignKey('cars.car_ID'))
    rental_start = db.Column(db.Date, nullable=False)
    rental_end = db.Column(db.Date, nullable=False)
    insurance_type = db.Column(db.String(20))
    excess = db.Column(db.Float(7))
    price = db.Column(db.Float(7), nullable=False)

    def __repr__(self):
        return ''.join([
            'Rental ', str(self.rental_ID)
              ])
