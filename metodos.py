from flask import render_template

def error(mensaje, error=400):
    return render_template("error.html", error=error, mensaje=mensaje), error