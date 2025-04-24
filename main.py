from flask import Flask

app= Flask(__name__)

from flask import Flask, request
from operaciones import suma

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1>Bienvenido a la calculadora</h1>
        <p>Selecciona una operación:</p>
        <ul>
            <li><a href="/suma?num1=5&num2=3">Suma</a></li>
            <li><a href="/resta?num1=10&num2=4">Resta</a></li>
            <li><a href="/multiplicacion?num1=6&num2=7">Multiplicación</a></li>
            <li><a href="/division?num1=20&num2=5">División</a></li>
        </ul>
    """

@app.route("/suma")
def ruta_suma():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    if num1 is None or num2 is None:
        return "Faltan parámetros"
    return f"<p>La suma de {num1} + {num2} es {suma(num1, num2)}</p>"

