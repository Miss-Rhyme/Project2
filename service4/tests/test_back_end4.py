import unittest

from flask import url_for
from flask_testing import TestCase

from os import getenv

from application import app, db

from application.models import Fortune


class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MY_SQL_USER'))+':'+str(getenv('MY_SQL_PASSWORD'))+'@'+str(getenv('MY_SQL_URL')))

        return app



class testpage(Testbase):

    def test_page(self):
        response =self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class test_query_database(TestBase):

    def test_result(self):

        self.assertEqual(Fortune.query.filter_by(code=A-1).first()"A-1")
