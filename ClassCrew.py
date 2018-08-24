from SQLConnection import DB
from ClassPerson import Person


class Crew(Person):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                 id_Normal_clients, dayStaying):
        Person.__init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                        id_Normal_clients)
        self.idCrew = idCrew
        self.dayStaying = dayStaying

    def InsertCrew(self, name, lastname, mail, password, dayStaying):
        Database = DB()
        crewCursor = Database.run("INSERT INTO Crew VALUES(NULL, %s)", str(dayStaying))
        self.idCrew = crewCursor.lastrowid
        Person.InsertPersonCrew(self, name, lastname, mail, password, self.idCrew)

    def UpdateCrew(self, name, lastname, mail, password, dayStaying):
        Database = DB()
        Person.UpdateCrewID(name, lastname, mail, password, self.idCrew)
        Database.run("UPDATE Crew SET dayStaying = %s WHERE idCrew = %s;", (str(dayStaying), str(self.idCrew)))

    @staticmethod
    def DeleteCrewFlight(idCrew):
        Database = DB()
        crew = Crew.SelectPersonNormalID(idCrew)
        Database.run("DELETE FROM Flight_has_Person WHERE idPersona = %s;", crew.idPersona)

    @staticmethod
    def DeleteCrew(idCrew):
        Database = DB()
        Crew.DeleteCrewFlight(idCrew)
        Person.DeleteCrewID(idCrew)
        Database.run("DELETE FROM Crew WHERE idCrew = %s;", str(idCrew))

    @staticmethod
    def SelectCrewID(idCrew):
        Database = DB()
        crewCursor = Database.run("SELECT * FROM Crew WHERE idCrew = %s;", idCrew)
        crewDict = crewCursor.fetchone()
        tmpCrew = Crew.GetCrew(crewDict)
        crew = Crew(tmpCrew[0], tmpCrew[1], tmpCrew[2], tmpCrew[3], tmpCrew[4], tmpCrew[5], tmpCrew[6], tmpCrew[7],
                    tmpCrew[8], tmpCrew[9])
        return crew

    @staticmethod
    def SelectCrew():
        Database = DB()
        crewCursor = Database.run("SELECT * FROM Crew;")
        crewDict = crewCursor.fetchall()
        crewLista = []
        for item in crewDict:
            tmpCrew = Crew.GetCrew(item)
            crew = Crew(tmpCrew[0], tmpCrew[1], tmpCrew[2], tmpCrew[3], tmpCrew[4], tmpCrew[5],tmpCrew[6], tmpCrew[7],
                        tmpCrew[8], tmpCrew[9])
            crewLista.append(crew)
        return crewLista

    @staticmethod
    def GetCrew(dic):
        person = Person.SelectPersonCrewID(dic["idCrew"])
        return person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7], person[8],\
               dic["dayStaying"]
