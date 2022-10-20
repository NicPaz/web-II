from http.client import PRECONDITION_FAILED
from flask import Flask, render_template, request
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

@app.route("/conversao", methods=["GET","POST"])
def converte():
    if request.method =='GET':
    #GET É O CASO QUANDO O USUARIO DIGITA A URL NO BROWSER
     return render_template("conversao.html")
    else:
        valorDol = float(request.form.get("dolar"))
        #TODO: pegar preço da cotação em:
        valorReais = valorDol * 5.24

    return render_template("conversao.html", valorReais = valorReais)

@app.route("/imc", methods=["GET","POST"])
def calculaImc():
    if request.method =='GET':
        return render_template("imc.html")
    else:
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        imc = peso / (altura * altura)
    return render_template("imc.html", imc = imc)



if __name__ == "__main__":
    app.run(debug=True)