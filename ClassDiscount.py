from SQLConnection import DB


class Discount(object):
    def __init__(self, idDiscount, percentDiscount):
        self.idDiscount = idDiscount
        self.percentDiscount = percentDiscount
