from SQLConnection import DB
from ClassPlane import Plane as ClassPlane


class Flight(object):
    def __init__(self, idFlight, destination, arrival, Plane):
        self.idFlight = idFlight
        self.destination = destination
        self.arrival = arrival
        self.Plane = Plane

    def InsertFlight(self):
        Database = DB()
        flightCursor = Database.run("INSERT INTO Flight VALUES(NULL, %s, %s, %s);", (self.destination, self.arrival,
                                                                                     str(self.Plane.idPlane)))
        self.idFlight = flightCursor.lastrowid

    def UpdateFlight(self, destination, arrival, Plane):
        Database = DB()
        Database.run("UPDATE Flight SET destination = %s, arrival = %s, idPlane = %s WHERE idFlight = %s;",
                     (destination, arrival, str(Plane.idPlane), str(self.idFlight)))
        self.destination = destination
        self.arrival = arrival
        self.Plane = Plane

    @staticmethod
    def DeleteFlight(idFlight):
        Database = DB()
        Database.run("DELETE FROM Flight WHERE idFlight = %s", str(idFlight))

    @staticmethod
    def SelectFlights():
        Database = DB()
        flightsCursor = Database.run("SELECT * FROM Flight;")
        flightsDict = flightsCursor.fetchall()
        flightList = []
        for item in flightsDict:
            tmpFlight = Flight.GetFlight(item)
            flight = Flight(tmpFlight[0], tmpFlight[1], tmpFlight[2], tmpFlight[3])
            flightList.append(flight)
        return flightList

    @staticmethod
    def SelectFlightsID(idFlight):
        Database = DB()
        flightsCursor = Database.run("SELECT * FROM Flight WHERE idFlight = %s;", str(idFlight))
        flightsDict = flightsCursor.fetchone()
        tmpFlight = Flight.GetFlight(flightsDict)
        flight = Flight(tmpFlight[0], tmpFlight[1], tmpFlight[2], tmpFlight[3])
        return flight

    @staticmethod
    def GetFlight(dic):
        Database = DB()
        planeCursor = Database.run("SELECT * FROM Plane WHERE idPlane = %s;", str(dic["idPlane"]))
        planeDict = planeCursor.fetchone()
        tmpPlane = ClassPlane.GetPlane(planeDict)
        Plane = ClassPlane(tmpPlane[0], tmpPlane[1], tmpPlane[2])
        return dic["idFlight"], dic["destination"], dic["arrival"], Plane
