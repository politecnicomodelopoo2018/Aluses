from SQLConnection import DB
from flask import Flask, render_template, request, redirect
from ClassCrew import Crew
from ClassNormalClients import NormalClients
from ClassDiscount import Discount


app = Flask(__name__)

Database = DB()
Database.SetConnection("localhost", "root", "alumno", "Aluses")


@app.route('/home')
def home():
    return render_template('Home.html')


@app.route('/crew')
def crew():
    listaCrew = Crew.SelectCrew()
    return render_template('Crew.html', listaCrew=listaCrew)


@app.route('/editarCrew', methods=['GET', 'POST'])
def editarCrew():
    idCrew = request.args.get('idCrew')
    return render_template('EditCrew.html', idCrew=idCrew)


@app.route('/editCrew', methods=['GET', 'POST'])
def editCrew():
    idCrew = request.form.get('idCrew')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    dayStaying = request.form.get('dayStaying')
    crewPerson = Crew.SelectCrewID(idCrew)
    crewPerson.UpdateCrew(name, lastname, mail, dayStaying, idCrew)
    return redirect('/crew')


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
    crewPerson = Crew("NULL", name, lastname, mail, password, idCrew, dayStaying)
    crewPerson.InsertCrew(name, lastname, mail, password, dayStaying)
    return redirect("/crew")


@app.route('/deleteCrew', methods=['GET', 'POST'])
def deleteCrew():
    idCrew = request.args.get('idCrew')
    Crew.DeleteCrew(idCrew)
    return redirect("/crew")


@app.route('/normalClient')
def NormalClient():
    listaNormalClients = NormalClients.SelectNormalClients()
    return render_template('NormalClient.html', listaNormalClients=listaNormalClients)

"""
@app.route('/editarCrew', methods=['GET', 'POST'])
def editarCrew():
    idCrew = request.args.get('idCrew')
    return render_template('EditCrew.html', idCrew=idCrew)


@app.route('/editCrew', methods=['GET', 'POST'])
def editCrew():
    idCrew = request.form.get('idCrew')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    dayStaying = request.form.get('dayStaying')
    crewPerson = Crew.SelectCrewID(idCrew)
    crewPerson.UpdateCrew(name, lastname, mail, dayStaying, idCrew)
    return redirect('/crew')
"""

@app.route('/insertarNormalClient')
def InsertarNormalClient():
    return render_template('InsertNormalClient.html')


@app.route('/insertNormalClient', methods=['GET', 'POST'])
def InsertNormalClient():
    idNormalClient = request.form.get('idNormalClient')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    password = request.form.get('password')
    idDiscount = request.form.get('idDiscount')
    DiscountObj = Discount.SelectDiscountsID(idDiscount)
    NormalClient = NormalClients("NULL", name, lastname, mail, password, idNormalClient, DiscountObj)
    NormalClient.InsertNormalClients(name, lastname, mail, password, DiscountObj)
    return redirect("/NormalClient")

"""
@app.route('/deleteCrew', methods=['GET', 'POST'])
def deleteCrew():
    idCrew = request.args.get('idCrew')
    Crew.DeleteCrew(idCrew)
    return redirect("/crew")
"""

if __name__ == '__main__':
    app.run(debug=True)
