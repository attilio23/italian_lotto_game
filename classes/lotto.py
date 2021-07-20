from classes.bill_type import BillType
from classes.city import City
from classes.print_helper import PrintHelper
from classes.ticket import Ticket
from classes.extraction import Extraction

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
    

    def winning_control(t, e):
        (c, n_g) = e.ticket_is_winning(t.b_t.type, t.c.city_name, t.n_p)
    
        if c:
            return "THE TICKET IS WINNING\n\n%s ON THE WHEEL OF %s\nTHE NUMBERS GUESSED ARE: %s\n" % (t.b_t.type.upper(), c.upper(), n_g)
        return "THE TICKET IS NOT WINNING\n"


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


    def extraction_creation():
        e = Extraction() 
        e.add_extraction()
        return e


    def extraction_and_tickets(ts, e):
        print((PrintHelper.print_line("LOTTO EXTRACTION:")) + "\n")
        print(e)
        
        if len(ts) == 1:
            print((PrintHelper.print_line("YOUR TICKET:")) + "\n")
        else:
            print((PrintHelper.print_line("YOUR TICKETS:")) + "\n")

        for t in ts:
            print(t)
            print(Lotto.winning_control(t, e))
    