from SQLConnection import DB
from ClassPerson import Person


class Crew(Person):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, dayStaying):
        Person.__init__(self, idPersona, name, lastname, mail, password)
        self.idCrew = idCrew
        self.dayStaying = dayStaying

    def InsertCrew(self, name, lastname, mail, password, dayStaying):
        Database = DB()
        crewCursor = Database.run("INSERT INTO Crew VALUES(NULL, %s)", str(dayStaying))
        self.idCrew = crewCursor.lastrowid
        Person.InsertPersonCrew(self, name, lastname, mail, password, self.idCrew)

    def UpdateCrew(self, name, lastname, mail, password, dayStaying):
        print(dayStaying)
        Database = DB()
        Person.UpdateCrewID(name, lastname, mail, password, self.idCrew)
        Database.run("UPDATE Crew SET dayStaying = %s WHERE idCrew = %s;", (str(dayStaying), str(self.idCrew)))

    @staticmethod
    def DeleteCrewFlight(idCrew):
        Database = DB()
        crew = Crew.SelectCrewID(idCrew)
        Database.run("DELETE FROM Flight_has_Person WHERE idPerson = %s;", crew.idPersona)

    @staticmethod
    def DeleteCrew(idCrew):
        Database = DB()
        Crew.DeleteCrewFlight(idCrew)
        Person.DeleteCrewID(idCrew)
        Database.run("DELETE FROM Crew WHERE idCrew = %s;", str(idCrew))

    @staticmethod
    def SelectCrewID(idCrew):
        Database = DB()
        crewCursor = Database.run("SELECT * FROM Crew WHERE idCrew = %s;", str(idCrew)) # OAJSSO
        crewDict = crewCursor.fetchone()
        tmpCrew = Crew.GetCrew(crewDict)
        person = Person.SelectPersonCrewID(tmpCrew[5])
        crew = Crew(person.idPersona, person.name, person.lastname, person.mail, person.password, tmpCrew[5],
                    tmpCrew[6])
        return crew

    @staticmethod
    def SelectCrew():
        Database = DB()
        crewCursor = Database.run("SELECT * FROM Crew;")
        crewDict = crewCursor.fetchall()
        crewLista = []
        for item in crewDict:
            tmpCrew = Crew.GetCrew(item)
            crew = Crew(tmpCrew[0], tmpCrew[1], tmpCrew[2], tmpCrew[3], tmpCrew[4], tmpCrew[5], tmpCrew[6])
            crewLista.append(crew)
        return crewLista

    @staticmethod
    def GetCrew(dic):
        person = Person.SelectPersonCrewID(dic["idCrew"])
        return person.idPersona, person.name, person.lastname, person.mail, person.password, dic["idCrew"],\
               dic["dayStaying"]
