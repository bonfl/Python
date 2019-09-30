from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!, este es el Index"

@app.route("/images")
def images():
    return "Acá las fotis"



if __name__ == "__main__":
    app.run()
