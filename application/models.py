from application import db, login_manager
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
    rentals = db.relationship('Rentals', backref='car_ID')

    def __repr__(self):
        return ''.join([
            'Car: ', self.colour, ' ', self.make, ' ', self.model, '\r\n',
            'Year produced: ', self.year, '\r\n',
            'Mileage: ', self.mileage, '\r\n',
            'Gearbox: ', self.gearbox, '\r\n',
            'Fuel type: ', self.fuel_type, '\r\n',
            'Engine size: ', self.engine_size, 'cc', '\r\n',
            'Number of doors: ', self.doors, '\r\n',
            'Number of seats: ', self.seats, '\r\n',
            'Price of car: ', self.price            
            ])

class Customers(db.Model):
    __tablename__ = 'customers'
    customer_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    home_address = db.Column(db.String(100), nullable=False)
    dl_number = db.Column(db.String(16), nullable=False, unique=True)
    creditcard_number = db.Column(db.Integer(), nullable=False)
    rentals = db.relationship('Rentals', backref='customer_ID')

    def __repr__(self):
        return ''.join([
            'Customer Name: ', self.first_name, ' ', self.last_name, '\r\n',
            'Home address: ', self.home_address, '\r\n',
            'Driving License Number: ', self.dl_number, '\r\n',
            'Bank details: ', self.creditcard_number
            ])

class Rentals(db.Model):
    __tablename__ = 'rentals'
    rental_ID = db.Column(db.Integer, primary_key=True)
    customer_ID = db.Column(db.Integer, db.ForeignKey('customers.customer_ID'))
    car_ID = db.Column(db.Integer, db.ForeignKey('cars.car_ID'))
    rental_start = db.Column(db.Date, nullable=False)
    rental_end = db.Column(db.Date, nullable=False)
    insurance_type = db.Column(db.String(20))
    excess = db.Column(db.Float(7))
    price = db.Column(db.Float(7), nullable=False)

    def __repr__(self):
        return ''.join([
            'Customer: ', self.customer_ID, '\r\n',
            'Car in use: ', self.car_ID, '\r\n',
            'Rental period: ', self.rental_start, ' - ', self.rental_end, '\r\n',
            'Type of insurance: ', self.insurance_type, '\r\n',
            'Excess amount: ', self.excess, '\r\n',
            'Price of rental: ', self.price
            ])
