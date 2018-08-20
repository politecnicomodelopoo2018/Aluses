from SQLConnection import DB


class FlightPerson(object):
    def __init__(self, Flight, Person, Seat):
        self.Flight = Flight
        self.Person = Person
        self.Seat = Seat
