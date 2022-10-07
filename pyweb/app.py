from http.client import PRECONDITION_FAILED
from flask import Flask, render_template
from datetime import datetime

#Flask é um framework web
#ele executa na url
# 127.0.0.1:5000 => localhost:5000


app = Flask(__name__)

@app.route("/")
def hello():
    agora = datetime.now()
    return f"<h1>Seja bem vindo - {agora}</h1>"

@app.route("/bomdia")
def bomdia():
    #return f"Bom dia"
    return render_template("index.html")

@app.route("/dolar")
def cotacao():
    valor = 5.21
    preco = 100
    total  =valor * preco
    return render_template("cotacao.html", valor=valor, preco=preco)


if __name__ == "__main__":
    app.run(debug=True)