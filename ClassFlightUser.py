from SQLConnection import DB
from ClassFlight import Flight
from ClassUser import User
from ClassSeats import Seats


class FlightUser(object):
    def __init__(self, FlightObj, UserObj, Seat):
        self.FlightObj = FlightObj
        self.UserObj = UserObj
        self.Seat = Seat

    def InsertFlightUser(self):
        Database = DB()
        Database.run("INSERT INTO Flight_has_User VALUES(%s, %s, %s);", (str(self.FlightObj.idFlight),
                                                                         str(self.UserObj.idUser),
                                                                         str(self.Seat.seatNumber)))

    def UpdateFlightUser(self, flightObj, userObj, seatObj):
        Database = DB()
        Database.run("UPDATE Flight_has_User SET seatNumber = %s, idFlight= %s, idUser= %s WHERE idFlight = %s"
                     "AND idUser = %s;", (str(seatObj.seatNumber), str(flightObj.idFlight), str(userObj.idUser),
                                          str(self.FlightObj.idFlight), str(self.UserObj.idUser)))
        self.FlightObj = flightObj
        self.UserObj = userObj
        self.Seat = seatObj

    @staticmethod
    def DeleteFlightUser(idFlight, idUser):
        Database = DB()
        Database.run("DELETE FROM Flight_has_User WHERE idFlight = %s AND idUser = %s;", (str(idFlight), str(idUser)))

    @staticmethod
    def SelectFlightUser():
        Database = DB()
        cursorFlightUser = Database.run("SELECT * FROM Flight_has_User;")
        dictFlightUser = cursorFlightUser.fetchall()
        listaFlightUser = []
        for item in dictFlightUser:
            tmpFlightUser = FlightUser.GetFlightUser(item)
            flightUser = FlightUser(tmpFlightUser[0], tmpFlightUser[1], tmpFlightUser[2])
            listaFlightUser.append(flightUser)
        return listaFlightUser

    @staticmethod
    def SelectFlightUserID(idFlight, idUser):
        Database = DB()
        cursorFlightUser = Database.run("SELECT * FROM Flight_has_User WHERE idFlight = %s AND idUser = %s;",
                                        (str(idFlight), str(idUser)))
        dictFlightUser = cursorFlightUser.fetchone()
        tmpFlightUser = FlightUser.GetFlightUser(dictFlightUser)
        flightUser = FlightUser(tmpFlightUser[0], tmpFlightUser[1], tmpFlightUser[2])
        return flightUser

    @staticmethod
    def GetFlightUser(dic):
        flight = Flight.SelectFlightsID(dic["idFlight"])
        user = User.SelectUserID(dic["idUser"])
        seat = Seats.SelectSeatsID(dic["seatNumber"])
        return flight, user, seat
