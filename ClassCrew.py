from SQLConnection import DB
from ClassPerson import Person


class Crew(Person):
    def __init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                 id_Normal_clients, dayStaying):
        Person.__init__(self, idPersona, name, lastname, mail, password, idCrew, id_VIP_clients, id_Disabled_clients,
                        id_Normal_clients)
        self.idCrew = idCrew
        self.dayStaying = dayStaying
