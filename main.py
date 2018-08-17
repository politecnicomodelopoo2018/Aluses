from SQLConnection import DB
from flask import Flask, render_template, request

app = Flask(__name__)

Database = DB()  # si quiero que lo ingreso el usuario lo meto en una ruta y lo que devuelve lo paso a objeto
Database.SetConnection("localhost", "root", "alumno", "Canal")  # En casa "", en el colegio "alumno"


if __name__ == '__main__':
    app.run(debug=True)
