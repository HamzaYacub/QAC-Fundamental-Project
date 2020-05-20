from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Cars, Rentals
from application.forms import AddCarForm, UpdateCarForm, RentCarForm, UpdateRentalForm

@app.route('/')
@app.route('/home')
def home():
    carData = Cars.query.all()
    print("hello")
    return render_template('home.html', title="Cars Available", cars=carData)

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    form = AddCarForm()
    if form.validate_on_submit():
        carData = Cars(
            make = form.make.data,
            model = form.model.data,
            year = form.year.data,
            mileage = form.mileage.data,
            gearbox = form.gearbox.data,
            doors = form.doors.data,
            seats = form.seats.data,
            fuel_type = form.fuel_type.data,
            engine_size = form.engine_size.data,
            colour = form.colour.data,
            price = form.price.data 
        )

        db.session.add(carData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('addCar.html', title="Add a Car", form=form)

@app.route('/update_car/<id>', methods=['GET', 'POST'])
def updateCar(id):
    form = UpdateCarForm()

    getCar = Cars.query.filter_by(car_ID=id).first()

    if form.validate_on_submit():
        getCar.make = form.make.data
        getCar.model = form.model.data
        getCar.year = form.year.data
        getCar.mileage = form.mileage.data
        getCar.gearbox = form.gearbox.data
        getCar.doors = form.doors.data
        getCar.seats = form.seats.data
        getCar.fuel_type = form.fuel_type.data
        getCar.engine_size = form.engine_size.data
        getCar.colour = form.colour.data
        getCar.price = form.price.data
        
        db.session.commit()
        return redirect(url_for('home'))

    elif request.method == 'GET':
        form.make.data = getCar.make
        form.model.data = getCar.model
        form.year.data = getCar.year
        form.mileage.data = getCar.mileage
        form.gearbox.data = getCar.gearbox
        form.doors.data = getCar.doors
        form.seats.data = getCar.seats
        form.fuel_type.data = getCar.fuel_type
        form.engine_size.data = getCar.engine_size
        form.colour.data = getCar.colour
        form.price.data = getCar.price

    return render_template('update.html', title='Update Car Information', form=form, car=getCar)

@app.route('/rent', methods=['GET', 'POST'])
def rentCar():
    form = RentCarForm()
    if form.validate_on_submit():
        rentData = Rentals(
            car = form.options.data,
            rental_start = form.rental_start.data,
            rental_end = form.rental_end.data,
            insurance_type = form.insurance_type.data,
            excess = form.excess.data,
            price = form.price.data
        )

        db.session.add(rentData)
        db.session.commit()

        return redirect(url_for('rental_history'))

    else:
        print(form.errors)
    
    return render_template('rent.html', title="Rent a Car", form=form)

@app.route('/rental_history')
def rental_history():
    
    rentData = Rentals.query.all()
    
    return render_template('rentalHistory.html', title="Rental History", rentals=rentData)

@app.route('/update_rental/<id>', methods=['GET', 'POST'])
def update_rental(id):
    form = UpdateRentalForm()

    getRental = Rentals.query.filter_by(rental_ID=id).first()

    if form.validate_on_submit():
        getRental.car = form.options.data
        getRental.rental_start = form.rental_start.data
        getRental.rental_end = form.rental_end.data
        getRental.insurance_type = form.insurance_type.data
        getRental.excess = form.excess.data
        getRental.price = form.price.data
        
        db.session.commit()
        return redirect(url_for('rental_history'))

    elif request.method == 'GET':
        form.options.data = getRental.car
        form.rental_start.data = getRental.rental_start
        form.rental_end.data = getRental.rental_end 
        form.insurance_type.data = getRental.insurance_type
        form.excess.data = getRental.excess
        form.price.data = getRental.price

    return render_template('updateRental.html', title='Update Rental Information', form=form)

@app.route('/update_car/<id>/delete', methods=["GET", "POST"])
def car_delete(id):
    car = Cars.query.filter_by(car_ID=id).first()
    rentals = Rentals.query.filter_by(car_ID=id).all()

    for rental in rentals:
        db.session.delete(rental)
    db.session.delete(car)

    db.session.commit() 

    return redirect(url_for('home'))

