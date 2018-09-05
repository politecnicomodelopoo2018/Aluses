from SQLConnection import DB
from ClassPlaneModel import PlaneModel


class Plane(object):
    def __init__(self, idPlane, Model, constructionDay):
        self.idPlane = idPlane
        self.Model = Model
        self.constructionDay = constructionDay

    def InsertPlane(self):
        Database = DB()
        planeCursor = Database.run("INSERT INTO Plane VALUES(NULL, %s, %s);", (str(self.Model.code),
                                                                               str(self.constructionDay)))
        self.idPlane = planeCursor.lastrowid

    def UpdatePlane(self, Model, constructionDay):
        Database = DB()
        Database.run("UPDATE Plane SET modelCode = %s, constructionDay = %s WHERE idPlane = %s;",
                     (str(Model.code), str(constructionDay), str(self.idPlane)))
        self.Model = Model
        self.constructionDay = constructionDay

    @staticmethod
    def DeletePlane(idPlane):
        Database = DB()
        Database.run("DELETE FROM Plane WHERE idPlane = %s;", str(idPlane))

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
    def SelectPlaneID(idPlane):
        Database = DB()
        planeCursor = Database.run("SELECT * FROM Plane WHERE idPlane = %s;", str(idPlane))
        planeDict = planeCursor.fetchone()
        tmpPlane = Plane.GetPlane(planeDict)
        plane = Plane(tmpPlane[0], tmpPlane[1], tmpPlane[2])
        return plane

    @staticmethod
    def GetPlane(dic):
        Model = PlaneModel.SelectPlaneModelsID(dic["modelCode"])
        return dic["idPlane"], Model, dic["constructionDay"]
