from flask import Flask

app = Flask (__name__)

@app.route('/')
def raiz():
    return "<p>Hello, World!!</p>"

@app.route('/add/<int:n1>/<int:n2>')
def add(n1:int,n2:int) -> str:
    return f"SOMA: {n1 + n2}"

@app.route('/sub/<int:n1>/<int:n2>')
def sub(n1:int,n2:int) -> str:
    return f"SUBTRACAO {n1 - n2}"

@app.route('/mult/<int:n1>/<int:n2>')
def mult(n1:int, n2:int) -> str:
    return f"MULTIPLICACAO {n1 * n2}"

@app.route('/div/<int:n1>/<int:n2>')
def div(n1:int, n2:int) -> str:
    if n2 == 0:
        return f"ERRO: DIVISAO POR 0"
    return f"DIVISAO {n1 / n2}"