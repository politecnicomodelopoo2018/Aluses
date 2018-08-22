from SQLConnection import DB


class Discount(object):
    def __init__(self, idDiscount, percentDiscount):
        self.idDiscount = idDiscount
        self.percentDiscount = percentDiscount

    @staticmethod
    def SelectDiscounts():
        Database = DB()
        discountCursor = Database.run("SELECT * FROM Discount;")
        discountDict = discountCursor.fetchall()
        discountList = []
        for item in discountDict:
            tmpDiscount = Discount.GetDiscount(item)
            discount = Discount(tmpDiscount[0], tmpDiscount[1])
            discountList.append(discount)

    @staticmethod
    def SelectDiscountsID(idDiscount):
        Database = DB()
        discountCursor = Database.run("SELECT * FROM Discount WHERE idDiscount = %s;", str(idDiscount))
        discountDict = discountCursor.fetchone()
        tmpDiscount = Discount.GetDiscount(discountDict)
        discount = Discount(tmpDiscount[0], tmpDiscount[1])
        return discount

    @staticmethod
    def GetDiscount(dic):
        return dic["idDiscount"], dic["percentDiscount"]
