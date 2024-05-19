from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

from .routes import setup_routes


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["MONGO_URI"] = (
        "mongodb://mongoadmin:secret@mongo:27017/admin?authSource=admin"
    )
    mongo = PyMongo(app)

    setup_routes(app, mongo)
    add_dummy_data(mongo.db)

    return app


def add_dummy_data(db):
    users_collection = db.users

    if users_collection.count_documents({}) == 0:
        dummy_users = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35},
            {"name": "Mark", "age": 22},
        ]

        users_collection.insert_many(dummy_users)
