from random import randrange
from classes.bill_type import BillType
from classes.city import City
from classes.print_helper import PrintHelper


class Ticket():
    def __init__(self, type = "", city_name = ""):
        self.b_t = BillType(type)
        self.c = City(city_name) 
        self.n_p = []

    
    def generate_numbers(self, num_amount):
        mn_amount = 1
        mx_amount = 10
        
        try:
            if mn_amount <= int(num_amount) <= mx_amount:
                mn = 1
                mx = 90
                i = 0
                
                while i < int(num_amount):
                    num = randrange(mn, mx + 1)
            
                    if not(num in self.n_p):
                        i = i + 1
                        self.n_p.append(num)  
                
                self.n_p.sort()
                i = 0

                while i < len(self.n_p):
                    self.n_p.insert(i, str(self.n_p.pop(i)))
                    i = i + 1
 
                return True

            return False
        except:
            return False   
    
    
    def __str__(self):
        delimeter = " "
        return PrintHelper.print_ticket(self.c.city_name, self.b_t.type, delimeter.join(self.n_p))