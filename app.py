from flask import Flask, send_file

app = Flask(__name__, static_url_path='/static')

@app.route('/notes')
def get_notes():
    return send_file('notes.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
