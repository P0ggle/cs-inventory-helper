from flask import jsonify

from .services import extract_data


def setup_routes(app):
    @app.route("/api/data", methods=["GET"])
    def get_data():
        extracted_data = extract_data()
        return jsonify(message=extracted_data)
