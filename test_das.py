import datetime
import psycopg2
import pytest
import requests
from requests import RequestException
from dbconnector import connect_to_db


class TestClass:

    @pytest.fixture()
    def setUp(self):
        connection = connect_to_db()
        yield connection
        connection.close()

    def test_connect_to_db(self, setUp):

        cur = setUp.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        assert db_version is not None





if __name__ == '__main__':
    pytest.main()

