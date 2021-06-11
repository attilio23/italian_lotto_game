  
from random import randrange


class NumbersPlayed():
    def __init__(self, numbers = ""):
        self.numbers = numbers
    
    
    def __str__(self):
        return "%s" % (self.numbers)
    
    
    def NumAmountIsValid(num_amount):
        mn_amount = 1
        mx_amount = 10
        
        try:
            if mn_amount <= int(num_amount) <= mx_amount:
                return True
            return False
        except:
            return False            
    
    
    def GenerateNumbers(self, num_amount):
        number_l = []
        mn = 1
        mx = 90
        i = 0
        
        while i < num_amount:
            num = randrange(mn, mx + 1)
            
            if not(num in number_l):
                i = i + 1
                number_l.append(num)  
        
        number_l.sort()
        delimeter = " "
        i = 0
        
        while i < len(number_l):
            num_s = str(number_l.pop(i))
            number_l.insert(i, num_s)
            i = i + 1
        
        self.numbers = delimeter.join(number_l)
        del number_l