from classes.bill_type import BillType
from classes.numbers_played import NumbersPlayed
from classes.city import City
from classes.print_output import PrintOutput


class Ticket():
    def __init__(self, type = "", city_name = "", numbers = "",):
        self.b_t = BillType(type)
        self.n_p = NumbersPlayed(numbers)
        self.c = City(city_name)    
    

    def SetNumbersPlayed(self):
        number_amount = input("How many numbers do you want to play? (max 10 per bill)\n\n")
        
        while not(NumbersPlayed.NumAmountIsValid(number_amount)):
            print("\nThe input is invalid.")
            number_amount = input("How many numbers do you want to play? (max 10 per bill)\n\n")    
        
        self.n_p.GenerateNumbers(int(number_amount))
        return int(number_amount) 
    
    
    def SetBillType(self, number_amount):
        bill_type = input("\nEnter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")
        
        while not(BillType.IsTypeValid(bill_type, number_amount)):
            print("\nThe input is invalid.")
            bill_type = input("Enter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")
        
        self.b_t.type = bill_type
    
    
    def SetCity(self):
        city = input("\nEnter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")
        
        while not(City.IsCityValid(city)):
            print("\nThe input is invalid.")
            city = input("Enter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")
        
        self.c.city_name = city

    
    def WinningControl(self, extraction):
        (c, n_g) = extraction.TicketIsWinning(self.b_t.type, self.c.city_name, self.n_p.numbers)
    
        if c:
            return "THE TICKET IS WINNING\n\n%s ON THE WHEEL OF %s\nTHE NUMBERS GUESSED ARE: %s\n" % (self.b_t.type.upper(), c.upper(), n_g)
        return "THE TICKET IS NOT WINNING\n"


    def __str__(self):
        return PrintOutput.PrintTicket(self.c.city_name, self.b_t.type, self.n_p.numbers)