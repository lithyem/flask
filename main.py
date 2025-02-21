from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
	return jsonify({"Choo Choo": "Welcome to your Flask app this rules!!"})

@app.route('/test')
def curious():
	return jsonify({"YOOOO": "OK"})

@app.route('/new_screen')
def new_screen():
    return jsonify({"message": "This is a new screen!"})


@app.route('/himom')
def himom():
    return jsonify({"message": "hi mom!"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
