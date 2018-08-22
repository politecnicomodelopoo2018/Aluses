from SQLConnection import DB
from ClassPlaneModel import PlaneModel


class Plane(object):
    def __init__(self, idPlane, Model, constructionDay):
        self.idPlane = idPlane
        self.Model = Model
        self.constructionDay = constructionDay

    def InsertPlane(self):
        Database = DB()
        planeCursor = Database.run("INSERT INTO Plane VALUES(NULL, " + self.Model + ", " + self.constructionDay + ")")
        self.idPlane = planeCursor.lastrowid

    def UpdatePlane(self, modelCode, constructionDay):
        Database = DB()
        Database.run("UPDATE Plane SET modelCode = " + modelCode + ", constructionDay = " + constructionDay +
                     " WHERE idPlane = " + self.idPlane + ";")
        self.__init__(self.idPlane, PlaneModel.SelectPlaneModelsID(modelCode), constructionDay)  # Preguntar a pruchi si muero o no

    @staticmethod
    def SelectPlanes():
        Database = DB()
        planeCursor = Database.run("SELECT * FROM Plane;")
        planeDict = planeCursor.fetchall()
        planesList = []
        for item in planeDict:
            tmpPlane = Plane.GetPlane(item)
            plane = Plane(tmpPlane[0], tmpPlane[1], tmpPlane[2])
            planesList.append(plane)
        return planesList

    @staticmethod
    def GetPlane(dic):
        Model = PlaneModel.SelectPlaneModelsID(dic["modelCode"])
        return dic["idPlane"], Model, dic["constructionDay"]
