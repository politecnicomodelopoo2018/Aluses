from SQLConnection import DB
from ClassPlane import Plane as ClassPlane


class Flight(object):
    def __init__(self, idFlight, destination, arrival, Plane):
        self.idFlight = idFlight
        self.destination = destination
        self.arrival = arrival
        self.Plane = Plane

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
    def GetFlight(dic):
        Database = DB()
        planeCursor = Database.run("SELECT * FROM Plane WHERE idPlane = " + dic["idPlane"] + ";")
        planeDict = planeCursor.fetchone()
        tmpPlane = ClassPlane.GetPlane(planeDict)
        Plane = ClassPlane(tmpPlane[0], tmpPlane[1], tmpPlane[2])
        return dic["idFlight"], dic["destination"], dic["arrival"], Plane
