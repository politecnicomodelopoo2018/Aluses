from SQLConnection import DB
from ClassPlaneModel import PlaneModel


class Plane(object):
    def __init__(self, idPlane, Model, constructionDay):
        self.idPlane = idPlane
        self.Model = Model
        self.constructionDay = constructionDay

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
        Database = DB()
        planeModelCursor = Database.run("SELECT * FROM PlaneModel WHERE code = " + dic["modelCode"] + ";")
        planeModelDict = planeModelCursor.fetchone()
        model = PlaneModel.GetPlaneModel(planeModelDict)
        Model = PlaneModel(model[0], model[1])
        return dic["idPlane"], Model, dic["constructionDay"]
