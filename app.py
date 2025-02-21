from flask import Flask, send_file, render_template, Response # type: ignore
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/notes')
def get_notes():
	notes_path = os.path.join(os.path.dirname(__file__), 'notes.txt')
	with open(notes_path, 'r') as file:
		content = file.read()
	return Response(content, mimetype='text/plain')

@app.route('/')
def index():
	return render_template('index.html')