from flask import Flask, render_template, request, sessions

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', name="Tutoz")
