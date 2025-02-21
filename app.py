from flask import Flask, send_file, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/notes')
def get_notes():
    return send_file('notes.txt', as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
