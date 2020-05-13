from application import db
from application.models import Cars, Customers, Rentals

db.drop_all()
db.create_all()
