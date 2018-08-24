from SQLConnection import DB
from flask import Flask, render_template, request
from ClassCrew import Crew


app = Flask(__name__)

Database = DB()
Database.SetConnection("localhost", "root", "alumno", "Aluses")


@app.route('/crew')
def crew():
    listaCrew = Crew.SelectCrew()
    return render_template('Crew.html', listaCrew=listaCrew)


@app.route('/editCrew', methods=['GET', 'POST'])
def editCrew():
    idCrew = request.form.get('idCrew')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    dayStaying = request.fomr.get('dayStaying')
    crewPerson = Crew.SelectPersonCrewID(idCrew)
    crewPerson.UpdateCrewID(name, lastname, mail, dayStaying, idCrew)
    return render_template('Crew.html')


@app.route('/insertarCrew')
def InsertarCrew():
    return render_template('InsertCrew.html')


@app.route('/insertCrew', methods=['GET', 'POST'])
def InsertCrew():
    idCrew = request.form.get('idCrew')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    password = request.form.get('password')
    dayStaying = request.form.get('dayStaying')
    crewPerson = Crew("NULL", name, lastname, mail, password, idCrew, "NULL", "NULL", "NULL", dayStaying)
    crewPerson.InsertCrew(name, lastname, mail, password, dayStaying)
    return render_template('Crew.html')


if __name__ == '__main__':
    app.run(debug=True)
