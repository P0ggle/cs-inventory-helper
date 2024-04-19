from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello this is served from flask! now running through docker!!!!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)
