from SQLConnection import DB


class Person(object):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                 id_Normal_clients):
        self.idPersona = idPersona
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password
        self.idCrew = idCrew
        self.id_VIP_clients = id_VIP_clients
        self.id_Disabled_clients = id_Disabled_clients
        self.id_Normal_clients = id_Normal_clients

    @staticmethod
    def SelectPersonNormalID(idNormalClient):
        Database = DB()
        normalCursor = Database.run("SELECT * FROM Normal_clients WHERE id_Normal_clients = %s;", idNormalClient)
