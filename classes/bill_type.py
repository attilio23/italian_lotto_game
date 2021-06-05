from classes.numbers_played import NumbersPlayed
class BillType():
    def __init__(self, type = ""):
        self.type = type
    def __str__(self):
        return "%s" % (self.type)
    def IsTypeValid(type, num_amount):
        tyId = {"Ambata" : 1, "Ambo" : 2, "Terno" : 3, "Quaterna" : 4, "Cinquina" : 5}
        if type in tyId.keys() and num_amount >= tyId[type]:
            return True
        return False