from SQLConnection import DB
from flask import Flask, render_template, request, redirect, session
from ClassUser import User
from ClassPlaneModel import PlaneModel
from ClassSeats import Seats
from ClassPlane import Plane
from ClassFlight import Flight
from ClassFlightUser import FlightUser

app = Flask(__name__)
app.secret_key = 'AlusesKey'

Database = DB()
Database.SetConnection("localhost", "root", "alumno", "Aluses")

Admin = User(1, 'Nicolas', 'Pruscino', 'nicolasPruscino@gmail.com', 'nico123', 1)


def Session():
    if not 'idUser' in session:
        session['idUser'] = session.get('idUser')
        session['name'] = session.get('name')
        session['lastname'] = session.get('lastname')
        session['mail'] = session.get('mail')
        session['password'] = session.get('password')
        session['administrador'] = session.get('administrador')


@app.route('/home', methods=['GET'])
def home():
    listaVuelos = Flight.SelectFlights()
    listaSalidas = []
    listaSalidasDepar = []
    listaLLegada = []
    listaLLegadaArriv = []
    listaDepartureDatetime = []
    listaArrivalDatetime = []
    active = False
    for item in listaVuelos:
        if item.departure not in listaSalidasDepar:
            listaSalidas.append(item)
            listaSalidasDepar.append(item.departure)
    for item in listaVuelos:
        if item.arrival not in listaLLegadaArriv:
            listaLLegada.append(item)
            listaLLegadaArriv.append(item.arrival)
    return render_template('UserHome.html', listaVuelos=listaVuelos, listaSalidas=listaSalidas,
                           listaLLegada=listaLLegada, active=active)


@app.route('/admin')
def admin():
    return render_template('AdminHome.html')


@app.route('/signIn')
def signIn():
    return render_template('SignIn.html')


@app.route('/signIn/confirm', methods=['POST'])
def confirmSignIn():
    mail = request.form.get('mail')
    password = request.form.get('password')
    user = User.SelectUserMailPassword(mail, password)
    Session()
    if user is None:
        return redirect('/signIn')
    if not user.idUser in session:
        session['idUser'] = user.idUser
        session['name'] = user.name
        session['lastname'] = user.lastname
        session['mail'] = user.mail
        session['password'] = user.password
        session['administrador'] = user.administrador
    if user.administrador == 1:
        return redirect('/admin')
    return redirect('/home')


@app.route('/signUp')
def signUp():
    return render_template('SignUp.html')


@app.route('/signUp/confirm', methods=['POST'])
def confirmSignUp():
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')
    if confirmPassword != password:
        return render_template('SignUp.html')
    user = User("NULL", name, lastname, mail, password)
    user.InsertUser(name, lastname, mail, password)
    if not user.idUser in session:
        session['idUser'] = user.idUser
        session['name'] = user.name
        session['lastname'] = user.lastname
        session['mail'] = user.mail
        session['password'] = user.password
        session['administrador'] = user.administrador
    return redirect('/home')


@app.route('/user')
def user():
    listaUser = User.SelectUser()
    return render_template('User.html', listaUser=listaUser)


@app.route('/user/insertarUser')
def InsertarUser():
    return render_template('InsertUser.html')


@app.route('/user/insertUser', methods=['GET', 'POST'])
def InsertUser():
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    password = request.form.get('password')
    user = User("NULL", name, lastname, mail, password)
    user.InsertUser(name, lastname, mail, password)
    return redirect("/user")


@app.route('/user/editarUser', methods=['GET', 'POST'])
def editarUser():
    idUser = request.args.get('idUser')
    return render_template('EditUser.html', idUser=idUser)


@app.route('/user/editUser', methods=['GET', 'POST'])
def editUser():
    idUser = request.form.get('idUser')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    mail = request.form.get('mail')
    password = request.form.get('password')
    user = User.SelectUserID(idUser)
    user.UpdateUser(name, lastname, mail, password)
    return redirect('/user')


@app.route('/user/deleteUser', methods=['GET', 'POST'])
def deleteUser():
    idUser = request.args.get('idUser')
    User.DeleteUser(idUser)
    return redirect("/user")


@app.route('/planeModel')
def planeModel():
    modelLista = PlaneModel.SelectPlaneModels()
    return render_template('PlaneModel.html', modelLista=modelLista)


@app.route('/planeModel/insertarModel')
def InsertarModel():
    return render_template('InsertModel.html')


@app.route('/planeModel/insertModel', methods=['GET', 'POST'])
def insertModel():
    seatQuantity = request.form.get('seatQuantity')
    Model = PlaneModel("NULL", seatQuantity)
    Model.InsertPlaneModel()
    return redirect("/planeModel")


@app.route('/planeModel/editarModel', methods=['GET'])
def editarModel():
    code = request.args.get('code')
    return render_template('EditModel.html', code=code)


@app.route('/planeModel/editModel', methods=['POST'])
def editModel():
    code = request.form.get('code')
    seatQuantity = request.form.get('seatQuantity')
    Model = PlaneModel.SelectPlaneModelsID(code)
    Model.UpdatePlaneModel(seatQuantity)
    return redirect('/planeModel')


@app.route('/planeModel/deleteModel', methods=['GET'])
def deleteModel():
    code = request.args.get('code')
    PlaneModel.DeletePlaneModel(code)
    return redirect('/planeModel')


@app.route('/seats')
def seat():
    seatLista = Seats.SelectSeats()
    return render_template('Seats.html', seatLista=seatLista)


@app.route('/seats/insertarSeats')
def insertarSeats():
    return render_template('InsertSeats.html')


@app.route('/seats/insertSeats', methods=['GET', 'POST'])
def insertSeats():
    modelCode = request.form.get('modelCode')
    seatClass = request.form.get('seatClass')
    model = PlaneModel.SelectPlaneModelsID(modelCode)
    Seat = Seats("NULL", model, seatClass)
    Seat.InsertSeats()
    return redirect('/seats')


@app.route('/seats/editarSeats', methods=['GET', 'POST'])
def editarSeats():
    seatNumber = request.args.get('seatNumber')
    return render_template('EditSeats.html', seatNumber=seatNumber)


@app.route('/seats/editSeats', methods=['GET', 'POST'])
def editSeats():
    seatNumber = request.form.get('seatNumber')
    modelCode = request.form.get('modelCode')
    seatClass = request.form.get('seatClass')
    model = PlaneModel.SelectPlaneModelsID(modelCode)
    Seat = Seats.SelectSeatsID(seatNumber)
    Seat.UpdateSeats(model, seatClass)
    return redirect('/seats')


@app.route('/seats/deleteSeats', methods=['GET'])
def deleteSeats():
    seatNumber = request.args.get('seatNumber')
    Seats.DeleteSeats(seatNumber)
    return redirect('/seats')


@app.route('/plane')
def plane():
    listaPlane = Plane.SelectPlanes()
    return render_template('Plane.html', listaPlane=listaPlane)


@app.route('/plane/insertarPlane')
def insertarPlane():
    return render_template('InsertPlane.html')


@app.route('/plane/insertPlane', methods=['POST'])  # hacer una lista seleccionable con los id a todo
def insertPlane():
    modelCode = request.form.get('modelCode')
    constructionDay = request.form.get('constructionDay')
    Model = PlaneModel.SelectPlaneModelsID(modelCode)
    plane = Plane("NULL", Model, constructionDay)
    plane.InsertPlane()
    return redirect('/plane')


@app.route('/plane/editarPlane', methods=['GET'])
def editarPlane():
    idPlane = request.args.get('idPlane')
    return render_template('EditPlane.html', idPlane=idPlane)


@app.route('/plane/editPlane', methods=['POST'])
def editPlane():
    idPlane = request.form.get('idPlane')
    modelCode = request.form.get('modelCode')
    constructionDay = request.form.get('constructionDay')
    Model = PlaneModel.SelectPlaneModelsID(modelCode)
    plane = Plane.SelectPlaneID(idPlane)
    plane.UpdatePlane(Model, constructionDay)
    return redirect('/plane')


@app.route('/plane/deletePlane', methods=['GET'])
def deltePlane():
    idPlane = request.args.get('idPlane')
    Plane.DeletePlane(idPlane)
    return redirect('/plane')


@app.route('/flight')
def flight():
    listaFlight = Flight.SelectFlights()
    return render_template('Flight.html', listaFlight=listaFlight)


@app.route('/flight/insertarFlight')
def insertarFlight():
    return render_template('InsertFlight.html')


@app.route('/flight/insertFlight', methods=['POST'])
def insertFlight():
    departure = request.form.get('departure')
    arrival = request.form.get('arrival')
    idPlane = request.form.get('idPlane')
    flightDepartureDatetime = request.form.get('flightDepartureDatetime')
    flightArrivalDatetime = request.form.get('flightArrivalDatetime')
    plane = Plane.SelectPlaneID(idPlane)
    flight = Flight("NULL", departure, arrival, plane, flightDepartureDatetime, flightArrivalDatetime)
    flight.InsertFlight()
    return redirect('/flight')


@app.route('/flight/editarFlight', methods=['GET'])
def editarFlight():
    idFlight = request.args.get('idFlight')
    return render_template('EditFlight.html', idFlight=idFlight)


@app.route('/flight/editFlight', methods=['POST'])
def editFlight():
    idFlight = request.form.get('idFlight')
    departure = request.form.get('departure')
    arrival = request.form.get('arrival')
    idPlane = request.form.get('idPlane')
    flightDepartureDatetime = request.form.get('flightDepartureDatetime')
    flightArrivalDatetime = request.form.get('flightArrivalDatetime')
    plane = Plane.SelectPlaneID(idPlane)
    flight = Flight.SelectFlightsID(idFlight)
    flight.UpdateFlight(departure, arrival, plane, flightDepartureDatetime, flightArrivalDatetime)
    return redirect('/flight')


@app.route('/flight/deleteFlight', methods=['GET'])
def deleteFlight():
    idFlight = request.args.get('idFlight')
    Flight.DeleteFlight(idFlight)
    return redirect('/flight')


@app.route('/flightUser')
def flightUser():
    listaFlightUser = FlightUser.SelectFlightUser()
    return render_template('FlightUser.html', listaFlightUser=listaFlightUser)


@app.route('/flightUser/insertarFlightUser')
def insertarFlightUser():
    return render_template('InsertFlightUser.html')


@app.route('/flightUser/insertFlightUser', methods=['POST'])
def insertFlightUser():
    idFlight = request.form.get('idFlight')
    idUser = request.form.get('idUser')
    seatNumber = request.form.get('seatNumber')
    flight = Flight.SelectFlightsID(idFlight)
    user = User.SelectUserID(idUser)
    seat = Seats.SelectSeatsID(seatNumber)
    flightUser = FlightUser(flight, user, seat)
    flightUser.InsertFlightUser()
    return redirect('/flightUser')


@app.route('/flightUser/editarFlightUser', methods=['GET'])
def editarFlightUser():
    idFlight = request.args.get('idFlight')
    idUser = request.args.get('idUser')
    return render_template('EditFlightUser.html', idFlight=idFlight, idUser=idUser)


@app.route('/flightUser/editFlightUser', methods=['POST'])
def editFlightUser():
    oldIDFlight = request.form.get('oldIDFlight')
    oldIDUser = request.form.get('oldIDUser')
    idFlight = request.form.get('idFlight')
    idUser = request.form.get('idUser')
    seatNumber = request.form.get('seatNumber')
    flight = Flight.SelectFlightsID(idFlight)
    user = User.SelectUserID(idUser)
    seat = Seats.SelectSeatsID(seatNumber)
    flightUser = FlightUser.SelectFlightUserID(oldIDFlight, oldIDUser)
    flightUser.UpdateFlightUser(flight, user, seat)
    return redirect('/flightUser')


@app.route('/flightUser/deleteFlightUser', methods=['GET'])
def deleteFlightUser():
    idFlight = request.args.get('idFlight')
    idUser = request.args.get('idUser')
    FlightUser.DeleteFlightUser(idFlight, idUser)
    return redirect('/flightUser')


if __name__ == '__main__':
    app.run(debug=True)
