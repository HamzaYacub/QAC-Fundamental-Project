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


class TestPosts(TestBase):

    def test_add_new_car(self):
        with self.client:
            response = self.client.post(
                '/add_car',
                data=dict(
                    make="Test make",
                    model="Test model",
                    year=('1997-11-04'),
                    mileage= 2200,
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




