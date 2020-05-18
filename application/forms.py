from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Cars, Rentals

class AddCarForm(FlaskForm):
    make = StringField('Make', 
            validators = [
                DataRequired(),
                Length(min=3, max=30)
                ]
    )
    model = StringField('Model', 
            validators = [
                Length(min=3, max=30)
                ]
    )
    year = DateField('Year', format='%Y-%m-%d' )

    mileage = IntegerField('Mileage', 
            validators = [
                DataRequired(),
                NumberRange(min=1, max=1000000)
                ]
    )
    gearbox = StringField('Gearbox', 
            validators = [
                DataRequired(),
                Length(min=3, max=20)
                ]
    )
    doors = IntegerField('Doors', 
            validators = [
                NumberRange(min=2, max=5)
                ]
    )
    seats = IntegerField('Seats', 
            validators = [
                NumberRange(min=2, max=10)
                ]
    )
    fuel_type = StringField('Fuel Type', 
            validators = [
                DataRequired(),
                Length(min=3, max=20)
                ]
    )
    engine_size = IntegerField('Engine size', 
            validators = [
                NumberRange(min=0, max=10000)
                ]
    )
    colour = StringField('Colour', 
            validators = [
                DataRequired(),
                Length(min=3, max=20)
                ]
    )
    price = IntegerField('Price', 
            validators = [
                DataRequired(),
                NumberRange(min=1, max=1000000)
                ]
    )
    
    add = SubmitField('Add Car')

class UpdateCarForm(FlaskForm):
    make = StringField('Make', 
            validators = [
                DataRequired(),
                Length(min=3, max=30)
                ]
    )
    model = StringField('Model', 
            validators = [
                Length(min=2, max=30)
                ]
    )
    year = DateField('Year', format='%Y-%m-%d' )

    mileage = IntegerField('Mileage', 
            validators = [
                DataRequired(),
                NumberRange(min=1, max=1000000)
                ]
    )
    gearbox = StringField('Gearbox', 
            validators = [
                DataRequired(),
                Length(min=3, max=20)
                ]
    )
    doors = IntegerField('Doors', 
            validators = [
                NumberRange(min=2, max=5)
                ]
    )
    seats = IntegerField('Seats', 
            validators = [
                NumberRange(min=2, max=10)
                ]
    )
    fuel_type = StringField('Fuel Type', 
            validators = [
                DataRequired(),
                Length(min=3, max=20)
                ]
    )
    engine_size = IntegerField('Engine size', 
            validators = [
                NumberRange(min=0, max=10000)
                ]
    )
    colour = StringField('Colour', 
            validators = [
                DataRequired(),
                Length(min=3, max=20)
                ]
    )
    price = IntegerField('Price', 
            validators = [
                DataRequired(),
                NumberRange(min=1, max=1000000)
                ]
    )

    update = SubmitField('Update Car')

def car_query():
    return Cars.query

class RentCarForm(FlaskForm):
    options = QuerySelectField(query_factory=car_query, allow_blank=False, get_label='car_ID')
    rental_start = DateField('Start', format='%Y-%m-%d' )
    rental_end = DateField('End of rental', format='%Y-%m-%d' )

    insurance_type = StringField('Type of Insurance', 
            validators = [
                DataRequired(),
                Length(min=3, max=20)
                ]
    )
    
    excess = IntegerField('Excess', 
            validators = [
                DataRequired(),
                NumberRange(min=1, max=1000000)
                ]
    )
    
    price = IntegerField('Price of Rental', 
            validators = [
                DataRequired(),
                NumberRange(min=1, max=1000000)
                ]
    )

    rent = SubmitField('Confirm Rental')

    def validate_date(self):
        if (self.rental_start.data>self.rental_end.data):
                raise ValidationError('Start date cannot be later than the end date!')
