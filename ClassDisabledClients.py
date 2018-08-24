from SQLConnection import DB
from ClassPerson import Person
from ClassDiscount import Discount


class DisabledClients(Person):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                 id_Normal_clients, DiscountObj):
        Person.__init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                        id_Normal_clients)
        self.id_Disabled_clients = id_Disabled_clients
        self.DiscountObj = DiscountObj

    def InsertDisabledClients(self, name, lastname, mail, password, idDiscount):
        Database = DB()
        disabledCursor = Database.run("INSERT INTO Disabled_clients VALUES(NULL, %s)", str(idDiscount))
        self.id_Disabled_clients = disabledCursor.lastrowid
        Person.InsertPersonDisabledClient(self, name, lastname, mail, password, self.id_Disabled_clients)

    def UpdateDisabledClients(self, name, lastname, mail, password, discount):
        Database = DB()
        Person.UpdateDisabledClientID(name, lastname, mail, password, self.id_Disabled_clients)
        Database.run("UPDATE Disabled_clients SET idDiscount = %s WHERE id_Disabled_clients = %s;",
                     (str(discount.idDiscount), str(self.id_Disabled_clients)))

    @staticmethod
    def DeleteDisabledClientFlight(idDisabledClient):
        Database = DB()
        Client = DisabledClients.SelectPersonDisabledID(idDisabledClient)
        Database.run("DELETE FROM Flight_has_Person WHERE idPersona = %s;", Client.idPersona)

    @staticmethod
    def DeleteDisabledClients(idDisabledClient):
        Database = DB()
        DisabledClients.DeleteDisabledClientFlight(idDisabledClient)
        Person.DeletePersonDisabledID(idDisabledClient)
        Database.run("DELETE FROM Disabled_clients WHERE id_Disabled_clients = %s;", str(idDisabledClient))

    @staticmethod
    def SelectDisabledClientsID(idDisabledClients):
        Database = DB()
        disabledCursor = Database.run("SELECT * FROM Disabled_Clients WHERE id_Disabled_clients = %s;",
                                      idDisabledClients)
        disabledDict = disabledCursor.fetchone()
        tmpClient = DisabledClients.GetClient(disabledDict)
        Client = DisabledClients(tmpClient[0], tmpClient[1], tmpClient[2], tmpClient[3], tmpClient[4], tmpClient[5],
                                 tmpClient[6], tmpClient[7], tmpClient[8], tmpClient[9])
        return Client

    @staticmethod
    def SelectDisabledClients():
        Database = DB()
        disabledCursor = Database.run("SELECT * FROM Disabled_Clients;")
        disabledDict = disabledCursor.fetchall()
        disabledLista = []
        for item in disabledDict:
            tmpClient = DisabledClients.GetClient(item)
            Client = DisabledClients(tmpClient[0], tmpClient[1], tmpClient[2], tmpClient[3], tmpClient[4], tmpClient[5],
                                     tmpClient[6], tmpClient[7], tmpClient[8], tmpClient[9])
            disabledLista.append(Client)
        return disabledLista

    @staticmethod
    def GetClient(dic):
        discount = Discount.SelectDiscountsID(dic["idDiscount"])
        person = Person.SelectPersonDisabledID(dic["id_Disabled_clients"])
        return person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7], person[8],\
               discount
