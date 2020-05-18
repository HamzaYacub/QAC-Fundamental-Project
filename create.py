from application import db
from application.models import Cars, Rentals

db.drop_all()
db.create_all()
