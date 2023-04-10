"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr8b1euhlq287d6nqg-a",
        database="dpg-cgpr8b1euhlq287d6nqg-a.oregon-postgres.render.com",
        user="todo_em3w_user",
        password="0M9KL0zhHrrlTW1XAzlDj9QGBrWodn3j")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
