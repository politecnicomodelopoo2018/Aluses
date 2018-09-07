from SQLConnection import DB


class User(object):
    def __init__(self, idUser, name, lastname, mail, password, administrador=0):
        self.idUser = idUser
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password
        self.administrador = administrador

    def InsertUser(self, name, lastname, mail, password, administrador=0):
        Database = DB()
        userCursor = Database.run("INSERT INTO User VALUES(NULL, %s, %s, %s, %s, %s)", (str(name), str(lastname),
                                                                                        str(mail), str(password),
                                                                                        administrador))
        self.idUser = userCursor.lastrowid

    def UpdateUser(self, name, lastname, mail, password):
        Database = DB()
        Database.run("UPDATE User SET name = %s, lastname = %s, mail = %s, password = %s WHERE idUser = %s;",
                     (str(name), str(lastname), str(mail), str(password), str(self.idUser)))

    @staticmethod
    def DeleteUserFlight(idUser):
        Database = DB()
        Database.run("DELETE FROM Flight_has_Person WHERE idUser = %s;", str(idUser))

    @staticmethod
    def DeleteUser(idUser):
        Database = DB()
        User.DeleteUserFlight(idUser)
        Database.run("DELETE FROM User WHERE idUser = %s;", str(idUser))

    @staticmethod
    def SelectUserID(idUser):
        Database = DB()
        userCursor = Database.run("SELECT * FROM User WHERE idUser = %s;", str(idUser))
        userDict = userCursor.fetchone()
        tmpUser = User.GetUser(userDict)
        user = User(tmpUser[0], tmpUser[1], tmpUser[2], tmpUser[3], tmpUser[4], tmpUser[5])
        return user

    @staticmethod
    def SelectUser():
        Database = DB()
        userCursor = Database.run("SELECT * FROM User;")
        userDict = userCursor.fetchall()
        userLista = []
        for item in userDict:
            tmpUser = User.GetUser(item)
            user = User(tmpUser[0], tmpUser[1], tmpUser[2], tmpUser[3], tmpUser[4], tmpUser[5])
            userLista.append(user)
        return userLista

    @staticmethod
    def SelectUserMailPassword(mail, password):
        Database = DB()
        userCursor = Database.run("SELECT * FROM User WHERE mail = %s AND password = %s;", (str(mail), str(password)))
        userDict = userCursor.fetchone()
        if userDict is None:
            return None
        tmpUser = User.GetUser(userDict)
        user = User(tmpUser[0], tmpUser[1], tmpUser[2], tmpUser[3], tmpUser[4], tmpUser[5])
        return user

    @staticmethod
    def GetUser(dic):
        return dic["idUser"], dic["name"], dic["lastname"], dic["mail"], dic["password"], dic["administrador"]
