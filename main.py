from SQLConnection import DB
from ClassPlaneModel import PlaneModel
from flask import Flask, render_template, request

app = Flask(__name__)

Database = DB()
Database.SetConnection("localhost", "root", "Patuco20", "Aluses")


if __name__ == '__main__':
    app.run(debug=True)
