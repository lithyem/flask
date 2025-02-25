from flask import Flask, jsonify, request # type: ignore
import os
#from app import app  # Import the Flask app from app.py

@app.route('/test')
def curious():
	return jsonify({"YOOOO": "OKman"})

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

if __name__ == '__main__':
	app.run(debug=True)
