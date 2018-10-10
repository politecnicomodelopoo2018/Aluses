from SQLConnection import DB
from ClassPlane import Plane as ClassPlane


class Flight(object):
    def __init__(self, idFlight, departure, arrival, Plane, flightDepartureDatetime, flightArrivalDatetime,
                 percentDiscount):
        self.idFlight = idFlight
        self.departure = departure
        self.arrival = arrival
        self.Plane = Plane
        self.flightDepartureDatetime = flightDepartureDatetime
        self.flightArrivalDatetime = flightArrivalDatetime
        self.percentDiscount = percentDiscount

    def InsertFlight(self):
        Database = DB()
        flightCursor = Database.run("INSERT INTO Flight VALUES(NULL, %s, %s, %s, %s, %s, %s);", (self.departure,
                                    self.arrival, str(self.Plane.idPlane), self.flightDepartureDatetime,
                                    self.flightArrivalDatetime, self.percentDiscount))
        self.idFlight = flightCursor.lastrowid

    def UpdateFlight(self, departure, arrival, Plane, flightDepartureDatetime, flightArrivalDatetime, percentDiscount):
        Database = DB()
        Database.run("UPDATE Flight SET departure = %s, arrival = %s, idPlane = %s, flightDepartureDatetime = %s,"
                     "flightArrivalDatetime = %s WHERE idFlight = %s;",
                     (departure, arrival, str(Plane.idPlane), str(self.idFlight), str(flightDepartureDatetime),
                      str(flightArrivalDatetime), str(percentDiscount)))
        self.departure = departure
        self.arrival = arrival
        self.Plane = Plane
        self.flightDepartureDatetime = flightDepartureDatetime
        self.flightArrivalDatetime = flightArrivalDatetime

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
            flight = Flight(tmpFlight[0], tmpFlight[1], tmpFlight[2], tmpFlight[3], tmpFlight[4], tmpFlight[5],
                            tmpFlight[6])
            flightList.append(flight)
        return flightList

    @staticmethod
    def SelectFlightsID(idFlight):
        Database = DB()
        flightsCursor = Database.run("SELECT * FROM Flight WHERE idFlight = %s;", str(idFlight))
        flightsDict = flightsCursor.fetchone()
        tmpFlight = Flight.GetFlight(flightsDict)
        flight = Flight(tmpFlight[0], tmpFlight[1], tmpFlight[2], tmpFlight[3], tmpFlight[4], tmpFlight[5],
                        tmpFlight[6])
        return flight

    @staticmethod
    def GetFlight(dic):
        Database = DB()
        planeCursor = Database.run("SELECT * FROM Plane WHERE idPlane = %s;", str(dic["idPlane"]))
        planeDict = planeCursor.fetchone()
        tmpPlane = ClassPlane.GetPlane(planeDict)
        Plane = ClassPlane(tmpPlane[0], tmpPlane[1], tmpPlane[2])
        return dic["idFlight"], dic["departure"], dic["arrival"], Plane, dic["flightDepartureDatetime"],\
               dic["flightArrivalDatetime"], dic["percentDiscount"]
