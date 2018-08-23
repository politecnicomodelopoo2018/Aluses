from SQLConnection import DB
from ClassPerson import Person
from ClassDiscount import Discount


class NormalClients(Person):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                 id_Normal_clients, DiscountObj):
        Person.__init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                        id_Normal_clients)
        self.id_Normal_clients = id_Normal_clients
        self.DiscountObj = DiscountObj

    def InsertNormalClients(self, name, lastname, mail, password, idDiscount):
        Database = DB()
        normalCursor = Database.run("INSERT INTO Normal_clients VALUES(NULL, %s)", str(idDiscount))
        self.id_Normal_clients = normalCursor.lastrowid
        Person.InsertPersonNormalClient(self, name, lastname, mail, password, self.id_Normal_clients)

    def UpdateNormalClients(self, name, lastname, mail, password, discount):
        Database = DB()
        Person.UpdateNormalClientID(name, lastname, mail, password, self.id_Normal_clients)
        Database.run("UPDATE Normal_clients SET idDiscount = %s WHERE id_Normal_clients = %s;",
                     (str(discount.idDiscount), str(self.id_Normal_clients)))

    @staticmethod
    def DeleteNormalClientFlight(idNormalClient):
        Database = DB()
        Client = NormalClients.SelectPersonNormalID(idNormalClient)
        Database.run("DELETE FROM Flight_has_Person WHERE idPersona = %s;", Client.idPersona)

    @staticmethod
    def DeleteNormalClients(idNormalClient):
        Database = DB()
        NormalClients.DeleteNormalClientFlight(idNormalClient)
        Person.DeletePersonNormalID(idNormalClient)
        Database.run("DELETE FROM Normal_clients WHERE id_Normal_clients = %s;", str(idNormalClient))

    @staticmethod
    def SelectNormalClientsID(idNormalClients):
        Database = DB()
        normalCursor = Database.run("SELECT * FROM Normal_Clients WHERE id_Normal_clients = %s;", idNormalClients)
        normalDict = normalCursor.fetchone()
        tmpClient = NormalClients.GetClient(normalDict)
        Client = NormalClients(tmpClient[0], tmpClient[1], tmpClient[2], tmpClient[3], tmpClient[4], tmpClient[5],
                               tmpClient[6], tmpClient[7], tmpClient[8], tmpClient[9])
        return Client

    @staticmethod
    def SelectNormalClients():
        Database = DB()
        normalCursor = Database.run("SELECT * FROM Normal_Clients;")
        normalDict = normalCursor.fetchall()
        normalLista = []
        for item in normalDict:
            tmpClient = NormalClients.GetClient(item)
            Client = NormalClients(tmpClient[0], tmpClient[1], tmpClient[2], tmpClient[3], tmpClient[4], tmpClient[5],
                                   tmpClient[6], tmpClient[7], tmpClient[8], tmpClient[9])
            normalLista.append(Client)
        return normalLista

    @staticmethod
    def GetClient(dic):
        discount = Discount.SelectDiscountsID(dic["idDiscount"])
        person = Person.SelectPersonNormalID(dic["id_Normal_clients"])
        return person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7], person[8],\
               discount
