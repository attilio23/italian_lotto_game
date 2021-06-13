from random import randrange


class NumbersPlayed():
    def __init__(self, numbers = "", num_amount = ""):
        self.numbers = numbers
        self.num_amount = num_amount
    
    
    def __str__(self):
        return "%s" % (self.numbers)
    
    
    def NumAmountIsValid(self, num_amount):
        mn_amount = 1
        mx_amount = 10
        
        try:
            if mn_amount <= int(num_amount) <= mx_amount:
                self.num_amount = num_amount
                return True
            
            return False
        except:
            return False            
    
    
    def GenerateNumbers(self):
        number_l = []
        mn = 1
        mx = 90
        i = 0
        
        while i < int(self.num_amount):
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