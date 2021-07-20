from classes.bill_type import BillType
from classes.city import City
from classes.print_helper import PrintHelper
from classes.ticket import Ticket

class Lotto():
    def set_number_played(t):
        number_amount = input("How many numbers do you want to play? (max 10 per bill)\n\n")
        b = t.generate_numbers(number_amount)
        
        while not(b):
            print("\nThe input is invalid.")
            number_amount = input("How many numbers do you want to play? (max 10 per bill)\n\n")    
            b = t.generate_numbers(number_amount)

    
    def set_bill_type(t):
        bill_type = input("\nEnter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")
        
        while not(t.b_t.is_type_valid(bill_type, len(t.n_p))):
            print("\nThe input is invalid.")
            bill_type = input("Enter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")
        
    
    def set_city(t):
        city = input("\nEnter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")
        
        while not(t.c.is_city_valid(city)):
            print("\nThe input is invalid.")
            city = input("Enter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")
    

    def ticket_creation(t_n):
        ts = []

        for i in range (t_n):
            ts.append(Ticket())

        i = 1

        for t in ts:
            print((PrintHelper.print_line("GENERATING THE TICKET " + str(i) + "...")) + "\n")
            Lotto.set_number_played(t)
            Lotto.set_bill_type(t)
            Lotto.set_city(t)
            i = i + 1

        return ts


    def print_tickets(ts):
        if len(ts) == 1:
            print((PrintHelper.print_line("YOUR TICKET:")) + "\n")
        else:
            print((PrintHelper.print_line("YOUR TICKETS:")) + "\n")

        for t in ts:
            print(t)