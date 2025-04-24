from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return '''

        Aplicación web con flask-afsr
        <h1>Calculadora</h1>
        <h3>opciones disponibles</h3>
        <ul>
            <li><a href="/suma">Suma</a></li>
            <li>Resta</li>
            <li>Multiplicacion</li>
            <li>División</li>
        
        
        </ul>

'''

@app.route("/suma")
def ruta_suma():
    return "página para aplicar la suma"

