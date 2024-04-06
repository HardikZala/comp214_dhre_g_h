from django.test import TestCase
from django.db import connection
# Create your tests here.

def test_db_connection():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM DH_STAFF FETCH FIRST 1 ROWS ONLY")
        row = cursor.fetchone()
    return row
