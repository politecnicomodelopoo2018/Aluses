from SQLConnection import DB


class PlaneModel(object):
    def __init__(self, code, quantity):
        self.code = code
        self.seatQuantity = quantity

    def InsertPlaneModel(self):
        Database = DB()
        planeModelCursor = Database.run("INSERT INTO PlaneModel VALUES(NULL, %s, %s);", (str(self.code),
                                                                                         str(self.seatQuantity)))
        self.code = planeModelCursor.lastrowid

    def UpdatePlaneModel(self, quantity):
        Database = DB()
        Database.run("UPDATE PlaneModel SET seatQuantity = %s WHERE code = %s;", (str(quantity), str(self.code)))
        self.seatQuantity = quantity

    @staticmethod
    def DeletePlaneModel(code):
        Database = DB()
        Database.run("DELETE FROM PlaneModel WHERE code = %s;", str(code))

    @staticmethod
    def SelectPlaneModelsID(modelCode):
        Database = DB()
        planeModelCursor = Database.run("SELECT * FROM PlaneModel WHERE code = %s;", modelCode)
        planeModelDict = planeModelCursor.fetchone()
        model = PlaneModel.GetPlaneModel(planeModelDict)
        Model = PlaneModel(model[0], model[1])
        return Model

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
