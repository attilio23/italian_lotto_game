from classes.lotto import Lotto 
from classes.ticket import Ticket
from classes.print_helper import PrintHelper


MIN_QUANTITY = 1
MAX_QUANTITY = 5


def start(tckt_nmbr):
  if not(tckt_nmbr):
    print("\n" + (PrintHelper.print_line("NO TICKETS WERE GENERATED")))
    quit()

  
  Lotto.print_tickets(Lotto.ticket_creation(tckt_nmbr))


if __name__ == "__main__":
  print((PrintHelper.print_line("LOTTO TICKET GENERATOR")) + "\n")
  ticket_quantity = input("\nEnter the number of tickets you want to generate: (min: 1, max: 5, 0: exit)\n\n")
  
  while ticket_quantity < str(MIN_QUANTITY - 1) or ticket_quantity > str(MAX_QUANTITY) or len(ticket_quantity) != 1:
    print("\nThe input is invalid.")
    ticket_quantity = input("Enter the number of tickets you want to generate: (min: 1, max: 5, 0: exit)\n\n") 
  
  start(int(ticket_quantity))