from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return "Aplicación web con flask"
