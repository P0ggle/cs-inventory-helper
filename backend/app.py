from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello this is served from flask!"})

if __name__ == '__main__':
    app.run(debug=True, port=5100)
