from SQLConnection import DB
from ClassPerson import Person
from ClassDiscount import Discount


class VIPClients(Person):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                 id_Normal_clients, DiscountObj):
        Person.__init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                        id_Normal_clients)
        self.id_VIP_clients = id_VIP_clients
        self.DiscountObj = DiscountObj

    def InsertVIPClients(self, name, lastname, mail, password, idDiscount):
        Database = DB()
        vipCursor = Database.run("INSERT INTO VIP_clients VALUES(NULL, %s)", str(idDiscount))
        self.id_VIP_clients = vipCursor.lastrowid
        Person.InsertPersonVIPClient(self, name, lastname, mail, password, self.id_VIP_clients)

    def UpdateVIPClients(self, name, lastname, mail, password, discount):
        Database = DB()
        Person.UpdateVIPClientID(name, lastname, mail, password, self.id_VIP_clients)
        Database.run("UPDATE VIP_clients SET idDiscount = %s WHERE id_VIP_clients = %s;",
                     (str(discount.idDiscount), str(self.id_VIP_clients)))

    @staticmethod
    def DeleteVIPClientFlight(idVIPClient):
        Database = DB()
        Client = VIPClients.SelectVIPClientsID(idVIPClient)
        Database.run("DELETE FROM Flight_has_Person WHERE idPersona = %s;", Client.idPersona)

    @staticmethod
    def DeleteVIPClients(idVIPClient):
        Database = DB()
        VIPClients.DeleteVIPClientFlight(idVIPClient)
        Person.DeletePersonVIPID(idVIPClient)
        Database.run("DELETE FROM VIP_clients WHERE id_VIP_clients = %s;", str(idVIPClient))

    @staticmethod
    def SelectVIPClientsID(idVIPClients):
        Database = DB()
        vipCursor = Database.run("SELECT * FROM VIP_Clients WHERE id_VIP_clients = %s;", idVIPClients)
        vipDict = vipCursor.fetchone()
        tmpClient = VIPClients.GetClient(vipDict)
        Client = VIPClients(tmpClient[0], tmpClient[1], tmpClient[2], tmpClient[3], tmpClient[4], tmpClient[5],
                            tmpClient[6], tmpClient[7], tmpClient[8], tmpClient[9])
        return Client

    @staticmethod
    def SelectVIPClients():
        Database = DB()
        vipCursor = Database.run("SELECT * FROM VIP_Clients;")
        vipDict = vipCursor.fetchall()
        vipLista = []
        for item in vipDict:
            tmpClient = VIPClients.GetClient(item)
            Client = VIPClients(tmpClient[0], tmpClient[1], tmpClient[2], tmpClient[3], tmpClient[4], tmpClient[5],
                                   tmpClient[6], tmpClient[7], tmpClient[8], tmpClient[9])
            vipLista.append(Client)
        return vipLista

    @staticmethod
    def GetClient(dic):
        discount = Discount.SelectDiscountsID(dic["idDiscount"])
        person = Person.SelectPersonVIPID(dic["id_VIP_clients"])
        return person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7], person[8],\
               discount
