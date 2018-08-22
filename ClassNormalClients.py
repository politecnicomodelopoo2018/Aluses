from SQLConnection import DB
from ClassPerson import Person
from ClassDiscount import Discount


class NormalClients(Person):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients, id_Normal_clients,
                 DiscountObj):
        Person.__init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                        id_Normal_clients)
        self.id_Normal_clients = id_Normal_clients
        self.DiscountObj = DiscountObj

    @staticmethod
    def SelectNormalClients():
        Database = DB()
        normalCursor = Database.run("SELECT * FROM Normal_Clients;")
        normalDict = normalCursor.fetchall()
        normalLista = []
        for item in normalDict:
            tmpClient = NormalClients.GetClient(item)
            Client = NormalClients(tmpClient[0], tmpClient[1], tmpClient[2], tmpClient[3], tmpClient[4], tmpClient[5],
                                   tmpClient[6], tmpClient[7], tmpClient[8])
            normalLista.append(Client)
        return normalLista

    @staticmethod
    def GetClient(dic):
        discount = Discount.SelectDiscountsID(dic["idDiscount"])
        return dic["idPersona"], dic["name"], dic["lastname"], dic["mail"], dic["password"], dic["idCrew"],\
               dic["id_VIP_Clients"], dic["id_Disabled_clients"], dic["id_Normal_clients"], discount
