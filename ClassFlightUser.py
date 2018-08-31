from SQLConnection import DB


class FlightPerson(object):
    def __init__(self, Flight, User, Seat):
        self.Flight = Flight
        self.User = User
        self.Seat = Seat
