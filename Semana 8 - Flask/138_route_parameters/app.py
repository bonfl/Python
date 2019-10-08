#importo libreria de Flask
from flask import Flask
#importo librería para hacer request
from flask import request

#creo mi programa
app = Flask(__name__)


#en el index, by defult si no se pone argumento "nombre", quedará como invitado
@app.route("/")
def hola_mundo(nombre="Invitado",edad="desconocida"):
    #sino, hago un request para leer en la url la entrada de nombre, ip:puerto/?nombre=nico
    nombre = request.args.get('nombre',nombre)
    edad = request.args.get('edad',edad)
#con esto puedo mostrar mi edad: http://127.0.0.1:5000/?nombre=nico&edad=27
    return "Hola {}, tu edad es {}".format(nombre,edad)


@app.route("/suma")
def suma(num1 = 0, num2 = 0):
    num1 = request.args.get('num1',num1)
    num2 = request.args.get('num2',num2)
    return "{} + {} es igual a {}".format(num1, num2, int(num1) + int(num2))


#llamo a mi programa
if __name__ == "__main__":
    app.run(debug = True) #debug encendido


#Acá funciona con esta URL: http://127.0.0.1:5000/suma?num1=2&num2=3
