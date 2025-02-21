from flask import Flask, send_file, render_template
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/notes')
def get_notes():
    notes_path = os.path.join(os.path.dirname(__file__), 'notes.txt')
    return send_file(notes_path, as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')
