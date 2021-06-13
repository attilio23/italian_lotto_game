from classes.numbers_played import NumbersPlayed


class BillType():
    tyId = {"Ambata" : 1, "Ambo" : 2, "Terno" : 3, "Quaterna" : 4, "Cinquina" : 5}
    
    
    def __init__(self, type = ""):
        self.type = type
    
    
    def __str__(self):
        return "%s" % (self.type)
    
    
    def IsTypeValid(self, type, num_amount, t_v = tyId):
        if type in t_v.keys() and int(num_amount) >= t_v[type]:
            self.type = type
            return True
        
        return False