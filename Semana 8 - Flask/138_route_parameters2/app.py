#importo libreria de Flask
from flask import Flask
#importo librería para hacer request
from flask import request

#creo mi programa
app = Flask(__name__)


#en el index, by defult si no se pone argumento "nombre", quedará como invitado
@app.route("/")
@app.route("/<nombre>")
def hola_mundo(nombre="Invitado"):
    return "Hola {}".format(nombre)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
def suma(num1 = 0, num2 = 0):
    return "{} + {} es igual a {}".format(num1, num2, num1 + num2)


#llamo a mi programa
if __name__ == "__main__":
    app.run(debug = True) #debug encendido


# Acá funciona con esta URL: http://127.0.0.1:5000/suma/1/3
# también el http://127.0.0.1:5000/nico
