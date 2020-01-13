import unittest

from flask import url_for
from flask_testing import TestCase

from os import getenv

from application import app


class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MY_SQL_USER'))+':'+str(getenv('MY_SQL_PASSWORD'))+'@'+str(getenv('MY_SQL_URL')))

        return app
    
class allthetests(TestBase):

    def test_page(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_random(self):
        
        assert type(number.codenumber()) is int
