from pathlib import Path

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

from .routes import setup_routes
from .services import insert_data_if_empty, load_data_from_json


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["MONGO_URI"] = (
        "mongodb://mongoadmin:secret@mongo:27017/testing?authSource=admin"
    )
    mongo = PyMongo(app)

    setup_routes(app, mongo)

    base_dir = Path(__file__).resolve().parent
    data_path = base_dir.parent / "data.json"

    data = load_data_from_json(data_path)
    insert_data_if_empty(mongo, data)

    return app
