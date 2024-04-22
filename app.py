from flask import Flask, render_template, request, session, redirect
from flask_session import Session

from metodos import *

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    res = eventos()
    return render_template('index.html', fondo="#fff", images=res)

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        res = val_login(request.form)
        
        if res[0]:
            app.logger.debug("Logeado")
            session["id_usuario"] = res[1]
            session["nombre"] = res[2]
            return redirect('/')
        else:
            app.logger.debug("Error al logear")
            return error(res[1])

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        res = val_register(request.form)
        if res[0]:
            return redirect('/')
        else:
            return error(res[1])