from SQLConnection import DB


class Person(object):
    def __init__(self, idPersona, name, lastname, mail, password):
        self.idPersona = idPersona
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password

    def InsertPersonNormalClient(self, name, lastname, mail, password, idNormalClient):
        Database = DB()
        normalCursor = Database.run("INSERT INTO Person VALUES(NULL, %s, %s, %s, %s, NULL, NULL, NULL, %s);",
                                    (str(name), str(lastname), str(mail), str(password), str(idNormalClient)))
        self.idPersona = normalCursor.lastrowid

    def InsertPersonDisabledClient(self, name, lastname, mail, password, idDisabledClient):
        Database = DB()
        disabledCursor = Database.run("INSERT INTO Person VALUES(NULL, %s, %s, %s, %s, NULL, NULL, %s, NULL);",
                                      (str(name), str(lastname), str(mail), str(password), str(idDisabledClient)))
        self.idPersona = disabledCursor.lastrowid

    def InsertPersonVIPClient(self, name, lastname, mail, password, idVIPClient):
        Database = DB()
        vipCursor = Database.run("INSERT INTO Person VALUES(NULL, %s, %s, %s, %s, NULL, %s, NULL, NULL);",
                                 (str(name), str(lastname), str(mail), str(password), str(idVIPClient)))
        self.idPersona = vipCursor.lastrowid

    def InsertPersonCrew(self, name, lastname, mail, password, idCrew):
        Database = DB()
        crewCursor = Database.run("INSERT INTO Person VALUES(NULL, %s, %s, %s, %s, %s, NULL, NULL, NULL);",
                                  (str(name), str(lastname), str(mail), str(password), str(idCrew)))
        self.idPersona = crewCursor.lastrowid

    @staticmethod
    def UpdateNormalClientID(name, lastname, mail, password, idNormalClient):
        Database = DB()
        Database.run("UPDATE Persona SET name = %s, lastname = %s, mail = %s, password = %s WHERE id_Normal_clients " +
                     "= %s;", (str(name), str(lastname), str(mail), str(password), str(idNormalClient)))

    @staticmethod
    def UpdateDisabledClientID(name, lastname, mail, password, idDisabledClient):
        Database = DB()
        Database.run("UPDATE Persona SET name = %s, lastname = %s, mail = %s, password = %s WHERE id_Disabled_clients "
                     + "= %s;", (str(name), str(lastname), str(mail), str(password), str(idDisabledClient)))

    @staticmethod
    def UpdateVIPClientID(name, lastname, mail, password, idVIPClient):
        Database = DB()
        Database.run("UPDATE Persona SET name = %s, lastname = %s, mail = %s, password = %s WHERE id_VIP_clients " +
                     "= %s;", (str(name), str(lastname), str(mail), str(password), str(idVIPClient)))

    @staticmethod
    def UpdateCrewID(name, lastname, mail, password, idCrew):
        Database = DB()
        Database.run("UPDATE Person SET name = %s, lastname = %s, mail = %s, password = %s WHERE id_Crew " +
                     "= %s;", (str(name), str(lastname), str(mail), str(password), str(idCrew)))

    @staticmethod
    def DeletePersonNormalID(idNormalClient):
        Database = DB()
        Database.run("DELETE FROM Normal_clients WHERE id_Normal_clients = %s;", str(idNormalClient))

    @staticmethod
    def DeletePersonDisabledID(idDisabledClient):
        Database = DB()
        Database.run("DELETE FROM Disable_clients WHERE id_Disabled_clients = %s;", str(idDisabledClient))

    @staticmethod
    def DeletePersonVIPID(idVIPClient):
        Database = DB()
        Database.run("DELETE FROM VIP_clients WHERE id_VIP_clients = %s;", str(idVIPClient))

    @staticmethod
    def DeleteCrewID(idCrew):
        Database = DB()
        Database.run("DELETE FROM Person WHERE id_Crew = %s;", str(idCrew))

    @staticmethod
    def SelectPersonNormalID(idNormalClient):
        Database = DB()
        normalCursor = Database.run("SELECT * FROM Normal_clients WHERE id_Normal_clients = %s;", str(idNormalClient))
        normalDict = normalCursor.fetchone()
        tmpPerson = Person.GetPerson(normalDict)
        person = Person(tmpPerson[0], tmpPerson[1], tmpPerson[2], tmpPerson[3], tmpPerson[4])
        return person

    @staticmethod
    def SelectPersonDisabledID(idDisabledClient):
        Database = DB()
        disabledCursor = Database.run("SELECT * FROM Disabled_clients WHERE id_Disabled_clients = %s;",
                                      str(idDisabledClient))
        disabledDict = disabledCursor.fetchone()
        tmpPerson = Person.GetPerson(disabledDict)
        person = Person(tmpPerson[0], tmpPerson[1], tmpPerson[2], tmpPerson[3], tmpPerson[4])
        return person

    @staticmethod
    def SelectPersonVIPID(idVIPClient):
        Database = DB()
        vipCursor = Database.run("SELECT * FROM VIP_clients WHERE id_VIP_clients = %s;", str(idVIPClient))
        vipDict = vipCursor.fetchone()
        tmpPerson = Person.GetPerson(vipDict)
        person = Person(tmpPerson[0], tmpPerson[1], tmpPerson[2], tmpPerson[3], tmpPerson[4])
        return person

    @staticmethod
    def SelectPersonCrewID(idCrew):
        Database = DB()
        crewCursor = Database.run("SELECT * FROM Person WHERE id_Crew = %s;", str(idCrew))
        crewDict = crewCursor.fetchone()
        tmpPerson = Person.GetPerson(crewDict)
        person = Person(tmpPerson[0], tmpPerson[1], tmpPerson[2], tmpPerson[3], tmpPerson[4])
        return person

    @staticmethod
    def GetPerson(dic):
        return dic["idPerson"], dic["name"], dic["lastname"], dic["mail"], dic["password"]
