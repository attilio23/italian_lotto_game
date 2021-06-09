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


    def __str__(self):
        s_ticket = ""
        s_lotto = ["┌──┐   ┌─────┐┌─────────┐┌─────────┐┌─────┐", \
                   "│  │   │ ┌─┐ │└──┐   ┌──┘└──┐   ┌──┘│ ┌─┐ │", \
                   "│  │   │ │ │ │   │   │      │   │   │ │ │ │", \
                   "│  └──┐│ └─┘ │   │   │      │   │   │ └─┘ │", \
                   "└─────┘└─────┘   └───┘      └───┘   └─────┘"]
        ticket_features = ["CITY: " + self.c.city_name, "TYPE: " + self.b_t.type]
        s_ticket = s_ticket + PrintOutput.OpenTable() + "\n"
        
        for line in s_lotto:
            s_ticket = s_ticket + PrintOutput.PrintTableLine(line) + "\n"
        
        s_ticket = s_ticket + PrintOutput.CloseOpenTable() + "\n"
        i = 0
        s_ticket = s_ticket + PrintOutput.PrintToLeft(ticket_features[i]) + "\n" 
        s_ticket = s_ticket + PrintOutput.PrintSeparator() + "\n"
        i = i + 1
        
        while i < len(ticket_features):
            s_ticket = s_ticket + PrintOutput.PrintToLeft(ticket_features[i]) + "\n"
            s_ticket = s_ticket + PrintOutput.PrintSeparator() + "\n"
            i = i + 1
        
        s_ticket = s_ticket + PrintOutput.PrintTableLine(self.n_p.numbers) + "\n"
        s_ticket = s_ticket + PrintOutput.CloseTable()
        return s_ticket