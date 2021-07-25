from random import randrange
from classes.bill_type import BillType
from classes.city import City
from classes.amount_played import AmountPlayed
from classes.print_helper import PrintHelper


class Ticket():
    def __init__(self, type = "", city_name = "", amount = ""):
        self.b_t = BillType(type)
        self.c = City(city_name) 
        self.n_p = []
        self.a_p = AmountPlayed(amount)


    def set_n_p(self, x):
        self.n_p = x.split()


    def set_b_t(self, x):
        self.b_t.type = x

    
    def set_c(self, x):
        self.c.city_name = x
    

    def set_a_p(self, x):
        self.a_p.amount = x


    @staticmethod
    def generate_numbers(num_amount):
        mn_amount = 1
        mx_amount = 10
        delimeter = " "
        num_generated = []

        try:
            if mn_amount <= int(num_amount) <= mx_amount:
                mn = 1
                mx = 90
                i = 0
                
                while i < int(num_amount):
                    num = randrange(mn, mx + 1)
            
                    if not(num in num_generated):
                        i = i + 1
                        num_generated.append(num)  
                
                num_generated.sort()
                i = 0

                while i < len(num_generated):
                    num_generated.insert(i, str(num_generated.pop(i)))
                    i = i + 1
 
                s_num_generated = delimeter.join(num_generated)
                del num_generated
                return s_num_generated

            return ""
        except:
            return ""   
    
    
    def __str__(self):
        delimeter = " "
        return PrintHelper.print_ticket(self.c.city_name, self.b_t.type, delimeter.join(self.n_p), self.a_p.amount)