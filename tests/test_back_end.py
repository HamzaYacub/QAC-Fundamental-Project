import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, db, bcrypt
from application.models import Cars, Rentals
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        car1 = Cars(
            make="Honda",
            model="Civic",
            year=('2006-04-11'),
            mileage=88000,
            gearbox="Manual",
            doors=5,
            seats=5,
            fuel_type="Petrol",
            engine_size=1800,
            colour="Silver",
            price=2300
        )

        car2 = Cars(
            make="Audi",
            model="RS3",
            year=('2018-11-04'),
            mileage=13000,
            gearbox="Auto",
            doors=5,
            seats=5,
            fuel_type="Diesel",
            engine_size=3000,
            colour="Black",
            price=23000
        )

        rental1 = Rentals(
            car_ID=2,
            rental_start=('2020-1-01'),
            rental_end=('2020-01-15'),
            insurance_type="Comprehensive",
            excess=500,
            price=1200
        )

        db.session.add(car1)
        db.session.add(car2)
        db.session.add(rental1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_rental_history_page_view(self):
        response = self.client.get(url_for('rental_history'))
        self.assertEqual(response.status_code, 200)

    def test_update_car_autofill(self):
        response = self.client.get('update_car/1')
        self.assertIn(b'1', response.data)

    def test_update_rental_autofill(self):
        response = self.client.get('update_rental/1')
        self.assertIn(b'2', response.data)


class TestPosts(TestBase):

    def test_add_new_car(self):
        with self.client:
            response = self.client.post(
                '/add_car',
                data=dict(
                    make="Test make",
                    model="Test model",
                    year=('1997-11-04'),
                    mileage=2200,
                    gearbox="Test gearbox",
                    doors=5,
                    seats=5,
                    fuel_type="Test fuel type",
                    engine_size=5000,
                    colour="Test Colour",
                    price=1000000
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test make', response.data)

    def test_update_car(self):
        with self.client:
            response = self.client.post(
                '/update_car/1',
                data=dict(
                    make="Test make",
                    model="Test model",
                    year=('1997-11-04'),
                    mileage=2200,
                    gearbox="Test gearbox",
                    doors=5,
                    seats=5,
                    fuel_type="Test fuel type",
                    engine_size=5000,
                    colour="Test Colour",
                    price=1000000
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test make', response.data)

    def test_rent_car(self):
        with self.client:
            response = self.client.post(
                '/rent',
                data=dict(
                    car="1",
                    rental_start=('2020-03-05'),
                    rental_end=('2020-03-15'),
                    insurance_type="Test gearbox",
                    excess=500,
                    price=800
                ),
                follow_redirects=True
            )
            self.assertIn(b'1', response.data)
    
    def test_update_rental(self):
        with self.client:
            response = self.client.post(
                '/update_rental/1',
                data=dict(
                    car="1",
                    rental_start=('2020-03-05'),
                    rental_end=('2020-03-15'),
                    insurance_type="Test gearbox",
                    excess=500,
                    price=800
                ),
                follow_redirects=True
            )
            self.assertIn(b'1', response.data)

    def test_delete_car(self):
        with self.client:
            response = self.client.post(
                '/update_car/1/delete',
                follow_redirects=True
            )
            count = Cars.query.count()
            self.assertEquals(count, 1)

    #validate dates entered in rent car and update rental forms
    #validate repr functions in models
    #redirect assertions
