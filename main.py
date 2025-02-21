from flask import Flask, jsonify, request
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

@app.route('/testing')
def testing():
    query_param = request.args.get('param')
    return jsonify({"query_param": query_param})

from app import app

if __name__ == '__main__':
    app.run(debug=True)
