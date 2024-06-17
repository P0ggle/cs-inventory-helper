from flask import Blueprint, jsonify


def setup_routes(app, mongo):
    main = Blueprint("main", __name__)

    @main.route("/api/data", methods=["GET"])
    def get_data():
        return jsonify({"temp": "temp"})

    @app.route("/api/cs-skins/first", methods=["GET"])
    def get_first_cs_skin():
        collection = mongo.db["cs-skins"]
        first_item = collection.find_one()
        if first_item:
            first_item["_id"] = str(first_item["_id"])
            return jsonify(first_item)
        else:
            return (jsonify({"error": "No items found in the collection"}),)

    app.register_blueprint(main)
