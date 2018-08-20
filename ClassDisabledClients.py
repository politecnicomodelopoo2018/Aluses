from SQLConnection import DB
from ClassPerson import Person


class DisabledClients(Person):
    def __init__(self, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients, id_Normal_clients,
                 Discount):
        Person.__init__(self, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                        id_Normal_clients)
        self.id_Disabled_clients = id_Disabled_clients
        self.Discount = Discount
