from SQLConnection import DB
from ClassPlaneModel import PlaneModel


class Seats(object):
    def __init__(self, seatNumber, Model, seatClass):
        self.seatNumber = seatNumber
        self.Model = Model
        self.seatClass = seatClass  # Primera, bussines, economica

    def InsertSeats(self):
        Database = DB()
        seatCursor = Database.run("INSERT INTO Seats VALUES(NULL, %s, %s);", (str(self.Model.code), self.seatClass))
        self.seatNumber = seatCursor.lastrowid

    def UpdateSeats(self, Model, seatClass):
        Database = DB()
        Database.run("UPDATE Seats SET modelCode = %s, seatClass = %s WHERE seatNumber = %s ;", (str(Model.code),
                                                                                                 seatClass,
                                                                                                 str(self.seatNumber)))
        self.Model = Model
        self.seatClass = seatClass

    @staticmethod
    def DeleteSeats(seatNumber):
        Database = DB()
        Database.run("DELETE * FROM Seats where seatNumber = %s;", seatNumber)

    @staticmethod
    def SelectSeats():
        Database = DB()
        seatsCursor = Database.run("SELECT * FROM Seats;")
        seatsDict = seatsCursor.fetchall()
        seatsList = []
        for item in seatsDict:
            tmpSeat = Seats.GetSeat(item)
            Seat = Seats(tmpSeat[0], tmpSeat[1], tmpSeat[2])
            seatsList.append(Seat)
        return seatsList

    @staticmethod
    def GetSeat(dic):
        Model = PlaneModel.SelectPlaneModelsID(dic["modelCode"])
        return dic["eatNumber"], Model, dic["seatClass"]
