from random import randrange
from classes.ticket import Ticket
from classes.bill_type import BillType
from classes.city import City
from classes.print_helper import PrintHelper


class Extraction():
    def __init__(self):
        self.wheels = {}
        
        for i in range(len(City.cities) - 1):
            self.wheels[City.cities[i]] = []
    
    
    def __str__(self):
        return PrintHelper.print_extraction(self.wheels)
    
    
    def add_extraction(self):
        mn = 1
        mx = 90
        numbers_per_wheel = 5
        
        for k in self.wheels:
            i = 0
            
            while i < numbers_per_wheel:
                number = randrange(mn, mx + 1)
                
                if len(str(number)) == 1 and not(" " + str(number) in self.wheels[k]):
                    self.wheels[k].append(" " + str(number))
                    i = i + 1
                elif len(str(number)) == 2 and not(str(number) in self.wheels[k]):
                    self.wheels[k].append(str(number)) 
                    i = i + 1
                    
    
    def ticket_is_winning(self, type, city_name, numbers):
        if city_name != "Tutte":
            j = 0
            c_numbers_guessed = 0
            s_numbers_guessed = ""
            numbers_guessed = []
            delimeter = " "
            
            while j < len(numbers) and c_numbers_guessed < BillType.tyId[type]:
                
                if numbers[j] in self.wheels[city_name]:
                    c_numbers_guessed = c_numbers_guessed + 1
                    numbers_guessed.append(str(numbers[j]))
                j = j + 1
            
            if c_numbers_guessed == BillType.tyId[type]:
                s_numbers_guessed = delimeter.join(numbers_guessed)
                del numbers_guessed
                return (city_name, s_numbers_guessed)
        
        else:
            for i in range(len(City.cities) - 1):
                j = 0
                c_numbers_guessed = 0
                s_numbers_guessed = ""
                numbers_guessed = []
                delimeter = " "

                while j < len(numbers) and c_numbers_guessed < BillType.tyId[type]:
                    
                    if numbers[j] in self.wheels[City.cities[i]]:
                        c_numbers_guessed = c_numbers_guessed + 1
                        numbers_guessed.append(str(numbers[j]))
                    j = j + 1
                
                if c_numbers_guessed == BillType.tyId[type]:
                    s_numbers_guessed = delimeter.join(numbers_guessed)
                    del numbers_guessed
                    return (City.cities[i], s_numbers_guessed)
        
        del numbers_guessed
        return ("", [])