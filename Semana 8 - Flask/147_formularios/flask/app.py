import json


from flask import Flask, render_template, url_for, redirect, request


#creo mi programa
app = Flask(__name__)


#en el index, by defult si no se pone argumento "nombre", quedará como invitado
@app.route("/")

def hola_mundo(nombre="Invitado"):

    try:
        data = json.loads(request.cookies.get("data"))
    except TypeError:
        data = {}
    else:
        nombre = data.get("nombre")

    contexto = {"nombre":nombre} #creo diccionario
    return render_template("index.html", **contexto)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
def suma(num1 = 0, num2 = 0):
    contexto = {"num1":num1, "num2":num2} # creo diccionario
    return render_template("suma.html", **contexto) #desempaqueto diccionario


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/enviar", methods=['POST'])    #este metodo indica que solo peude ser usado internamente
def enviar():
    response = redirect(url_for("hola_mundo"))
    response.set_cookie("data", json.dumps(dict(request.form.items())))
    response.set_cookie("sesion", "Informacion de sesion")
    return response


#llamo a mi programa
if __name__ == "__main__":
    app.run(debug = True) #debug encendido


# Acá funciona con esta URL: http://127.0.0.1:5000/suma/1/3
# también el http://127.0.0.1:5000/nico
