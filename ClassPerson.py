from SQLConnection import DB


class Person(object):
    def __init__(self, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients, id_Normal_clients):
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password
        self.idCrew = idCrew
        self.id_VIP_clients = id_VIP_clients
        self.id_Disabled_clients = id_Disabled_clients
        self.id_Normal_clients = id_Normal_clients
