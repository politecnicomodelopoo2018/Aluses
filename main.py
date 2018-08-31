from SQLConnection import DB
from flask import Flask, render_template, request, redirect
from ClassUser import User
from ClassPlaneModel import PlaneModel

app = Flask(__name__)

Database = DB()
Database.SetConnection("localhost", "root", "alumno", "Aluses")


@app.route('/home')
def home():
    return render_template('Home.html')


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


if __name__ == '__main__':
    app.run(debug=True)
