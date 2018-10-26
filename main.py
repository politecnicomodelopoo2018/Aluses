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
# mostrar bustacas para seleccionar(super bado)
Database = DB()
Database.SetConnection("localhost", "root", "alumno", "Aluses")


# user = User('Nicolas', 'Pruscino', 'nicolasPruscino@gmail.com', 'nico123', 1)  # ya esta creado, solo para fijarse nombre y contra
# user.InsertUser('Nicolas', 'Pruscino', 'nicolasPruscino@gmail.com', 'nico123', 1)
# user = User('Sebastian', 'Elustondo', 'sebastianelustondo@gmail.com', 'Patuco20', 1)  # ya esta creado, solo para fijarse nombre y contra
# user.InsertUser('Sebastian', 'Elustondo', 'sebastianelustondo@gmail.com', 'Patuco20', 1)


def Session():
    if not 'idUser' in session:
        session['idUser'] = session.get('idUser')


@app.route('/home', methods=['GET'])
def home():
    active = False
    user = User('', '', '', '', '')
    if 'idUser' in session:
        active = True
        user = User.SelectUserID(session['idUser'])
    listaVuelosUser = FlightUser.SelectUsers(user.idUser)
    return render_template('UserHome.html', active=active, admin=user.administrador, listaVuelosUser=listaVuelosUser)


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
    if user is None:
        return redirect('/signIn')
    if not user.idUser in session:
        session['idUser'] = user.idUser
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
    return redirect('/home')


@app.route('/logOutSesion')
def logOut():  
    session.pop('idUser', None)
    return redirect('/home')


@app.route('/personalizaTuViaje', methods=['POST', 'GET'])
def personalizarViaje():
    salida = request.form.get('salida')
    llegada = request.form.get('llegada')
    fechaIda = request.form.get('fechaIda')
    fechaVuelta = request.form.get('fechaVuelta')
    idSeat = request.form.get('asiento')

    flight = Flight.BuscarViaje(salida, llegada, fechaIda, fechaVuelta)

    return render_template('personalizarViaje.html', flight=flight, idSeat=idSeat)


@app.route('/elegirSalida')
def elegirSalida():
    listaVuelos = Flight.SelectFlights()
    listaSalidas = []
    for item in listaVuelos:
        if item.departure not in listaSalidas:
            listaSalidas.append(item.departure)
    return render_template('elegirSalida.html', listaSalidas=listaSalidas)


@app.route('/elegirLLegada', methods=['POST', 'GET'])
def elegirLLegada():
    salida = request.form.get('salida')
    listaFlight = Flight.BuscarSalida(salida)
    listaLLegadas = []
    for item in listaFlight:
        if item.arrival not in listaLLegadas:
            listaLLegadas.append(item.arrival)
    return render_template('elegirLLegada.html', listaLLegadas=listaLLegadas, salida=salida)


@app.route('/elegirFechaIda', methods=['POST', 'GET'])
def elegirFechaIda():
    salida = request.form.get('salida')
    llegada = request.form.get('llegada')
    listaFlight = Flight.BuscarSalidaLLegada(salida, llegada)
    listaFechaIda = []
    for item in listaFlight:
        if item.flightDepartureDatetime not in listaFechaIda:
            listaFechaIda.append(item.flightDepartureDatetime)
    return render_template('elegirFechaIda.html', listaFechaIda=listaFechaIda, llegada=llegada, salida=salida)


@app.route('/elegirFechaVuelta', methods=['POST', 'GET'])
def elegirFechaVuelta():
    salida = request.form.get('salida')
    llegada = request.form.get('llegada')
    fechaIda = request.form.get('fechaIda')
    listaFlight = Flight.BuscarSalidaLLegadaFechaIda(salida, llegada, fechaIda)
    listaFechaVuelta = []
    for item in listaFlight:
        if item.flightArrivalDatetime not in listaFechaVuelta:
            listaFechaVuelta.append(item.flightArrivalDatetime)
    return render_template('elegirFechaVuelta.html', listaFechaVuelta=listaFechaVuelta, fechaIda=fechaIda,
                           llegada=llegada, salida=salida)


@app.route('/elegirAsiento', methods=['POST', 'GET'])
def elegirAsiento():
    salida = request.form.get('salida')
    llegada = request.form.get('llegada')
    fechaIda = request.form.get('fechaIda')
    fechaVuelta = request.form.get('fechaVuelta')
    listaFlight = Flight.BuscarSalidaLLegadaFechaIdaFechaVuelta(salida, llegada, fechaIda, fechaVuelta)
    asientos = Seats.SelectSeats()
    listaAsientos = []
    for item in listaFlight:
        for item2 in asientos:
            if item2.Model.code == item.Plane.Model.code:
                listaAsientos.append(item2)
    return render_template('elegirAsiento.html', listaAsientos=listaAsientos, salida=salida, llegada=llegada,
                           fechaIda=fechaIda, fechaVuelta=fechaVuelta)


@app.route('/reservarViaje', methods=['POST', 'GET'])
def reservarViaje():
    idFlight = request.form.get('idFlight')
    idSeat = request.form.get('idSeat')
    flight = Flight.SelectFlightsID(idFlight)
    user = User.SelectUserID(session['idUser'])
    seat = Seats.SelectSeatsID(idSeat)
    flightUser = FlightUser(flight, user, seat)
    if flightUser not in FlightUser.SelectFlightUser():
        flightUser.InsertFlightUser()
    return redirect('home')


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
    percentDiscount = request.form.get('percentDiscount')
    plane = Plane.SelectPlaneID(idPlane)
    flight = Flight("NULL", departure, arrival, plane, flightDepartureDatetime, flightArrivalDatetime, percentDiscount)
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
    percentDiscount = request.form.get('percentDiscount')
    plane = Plane.SelectPlaneID(idPlane)
    flight = Flight.SelectFlightsID(idFlight)
    flight.UpdateFlight(departure, arrival, plane, flightDepartureDatetime, flightArrivalDatetime, percentDiscount)
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
