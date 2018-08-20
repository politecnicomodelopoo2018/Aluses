from SQLConnection import DB
from ClassPlaneModel import PlaneModel


class Seats(object):
    def __init__(self, seatNumber, Model, seatClass):
        self.seatNumber = seatNumber
        self.Model = Model
        self.seatClass = seatClass  # Primera, bussines, economica

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
        Database = DB()
        planeModelCursor = Database.run("SELECT * FROM PlaneModel WHERE code = " + dic["modelCode"] + ";")
        planeModelDict = planeModelCursor.fetchone()
        model = PlaneModel.GetPlaneModel(planeModelDict)
        Model = PlaneModel(model[0], model[1])
        return dic["eatNumber"], Model, dic["seatClass"]
