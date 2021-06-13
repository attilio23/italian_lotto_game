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
        
        while not(self.n_p.NumAmountIsValid(number_amount)):
            print("\nThe input is invalid.")
            number_amount = input("How many numbers do you want to play? (max 10 per bill)\n\n")    
        
        self.n_p.GenerateNumbers()

    
    def SetBillType(self):
        bill_type = input("\nEnter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")
        
        while not(self.b_t.IsTypeValid(bill_type, self.n_p.num_amount)):
            print("\nThe input is invalid.")
            bill_type = input("Enter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")
        
    
    def SetCity(self):
        city = input("\nEnter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")
        
        while not(self.c.IsCityValid(city)):
            print("\nThe input is invalid.")
            city = input("Enter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")

    
    def WinningControl(self, extraction):
        (c, n_g) = extraction.TicketIsWinning(self.b_t.type, self.c.city_name, self.n_p.numbers)
    
        if c:
            return "THE TICKET IS WINNING\n\n%s ON THE WHEEL OF %s\nTHE NUMBERS GUESSED ARE: %s\n" % (self.b_t.type.upper(), c.upper(), n_g)
        return "THE TICKET IS NOT WINNING\n"


    def __str__(self):
        return PrintOutput.PrintTicket(self.c.city_name, self.b_t.type, self.n_p.numbers)