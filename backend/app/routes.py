from flask import Blueprint, jsonify

from .services import extract_data


def setup_routes(app, mongo):
    main = Blueprint("main", __name__)

    @main.route("/api/data", methods=["GET"])
    def get_data():
        extracted_data = extract_data()
        return jsonify(message=extracted_data)

    @main.route("/")
    def home():
        return jsonify({"message": "Welcome to the Flask app with MongoDB!"})

    @main.route("/users")
    def get_users():
        users = mongo.db.users.find()
        users_list = [{"name": user["name"], "age": user["age"]} for user in users]
        return jsonify(users_list)

    app.register_blueprint(main)
