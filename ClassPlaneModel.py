from SQLConnection import DB


class PlaneModel(object):
    def __init__(self, code, quantity):
        self.code = code
        self.seatQuantity = quantity

    def InsertPlaneModel(self):
        Database = DB()
        planeModelCursor = Database.run("INSERT INTO PlaneModel VALUES(NULL" + self.code + ", " + self.seatQuantity +
                                        ");")
        self.code = planeModelCursor.lastrowid

    def UpdatePlaneModel(self, code, quantity):
        Database = DB()
        Database.run("UPDATE PlaneModel SET seatQuantity = " + str(quantity) + " WHERE code = " + str(code) + ";")
        self.__init__(code, quantity)

    @staticmethod
    def DeletePlaneModel(code):
        Database = DB()
        Database.run("DELETE FROM PlaneModel WHERE code = + " + code + ";")

    @staticmethod
    def SelectPlaneModels():
        Database = DB()
        planeModelCursor = Database.run("SELECT * FROM PlaneModel;")
        planeModelDict = planeModelCursor.fetchall()
        planeModelList = []
        for item in planeModelDict:
            tmpModel = PlaneModel.GetPlaneModel(item)
            Model = PlaneModel(tmpModel[0], tmpModel[1])
            planeModelList.append(Model)
        return planeModelList

    @staticmethod
    def GetPlaneModel(dic):
        return dic["code"], dic["quantity"]
