from cs50 import SQL
from flask import Flask, render_template, request, session, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session

from metodos import *

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///src/database/database.sqlite3")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        usr = request.form.get("username")
        psw = usr+request.form.get("password")
        res = db.execute("SELECT * FROM usuarios WHERE username=?", usr)

        if (len(res) == 1):
            hash_psw = res[0]['hash']
            if check_password_hash(hash_psw, psw):
                app.logger.debug("Logeado")
                session["id_usuario"] = res[0]['id']
                session["usuario"] = res[0]['username']
                return redirect('/')
        
        app.logger.debug("Error al logear")
        return error("Nombre o contraseña incorrectos.")

    return render_template('index.html')

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")