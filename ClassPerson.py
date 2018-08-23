from SQLConnection import DB


class Person(object):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                 id_Normal_clients):
        self.idPersona = idPersona
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password
        self.idCrew = idCrew
        self.id_VIP_clients = id_VIP_clients
        self.id_Disabled_clients = id_Disabled_clients
        self.id_Normal_clients = id_Normal_clients

    def InsertPersonNormalClient(self, name, lastname, mail, password, idNormalClient):
        Database = DB()
        normalCursor = Database.run("INSERT INTO Person VALUES(NULL, %s, %s, %s, %s, NULL, NULL, NULL, %s);",
                                    (str(name), str(lastname), str(mail), str(password), str(idNormalClient)))
        self.idPersona = normalCursor.lastrowid

    @staticmethod
    def UpdateNormalClientID(name, lastname, mail, password, idNormalClient):
        Database = DB()
        Database.run("UPDATE Persona SET name = %s, lastname = %s, mail = %s, password = %s WHERE id_Normal_clients " +
                     "= %s;", (str(name), str(lastname), str(mail), str(password), str(idNormalClient)))

    @staticmethod
    def DeletePersonNormalID(idNormalClient):
        Database = DB()
        Database.run("DELETE FROM Normal_clients WHERE id_Normal_clients = %s;", str(idNormalClient))

    @staticmethod
    def SelectPersonNormalID(idNormalClient):
        Database = DB()
        normalCursor = Database.run("SELECT * FROM Normal_clients WHERE id_Normal_clients = %s;", str(idNormalClient))
        normalDict = normalCursor.fetchone()
        tmpPerson = Person.GetPerson(normalDict)
        person = Person(tmpPerson[0], tmpPerson[1], tmpPerson[2], tmpPerson[3], tmpPerson[4], tmpPerson[5],
                                   tmpPerson[6], tmpPerson[7], tmpPerson[8])
        return person

    @staticmethod
    def GetPerson(dic):
        return dic["idPersona"], dic["name"], dic["lastname"], dic["mail"], dic["password"], dic["idCrew"], \
        dic["id_VIP_Clients"], dic["id_Disabled_clients"],