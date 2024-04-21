from cs50 import SQL
from flask import Flask, render_template, request, session, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///src/database/database.sqlite3")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        usr = request.form.get("username")
        psw = request.form.get("password")
        
        res = db.execute("SELECT * FROM usuarios WHERE username=? AND hash=?", usr, psw)
        if (len(res) == 1):
            app.logger.debug("Logeado")
        else:
            app.logger.debug("Usuario o contraseña incorrectos")
    
    return render_template('login.html')

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")