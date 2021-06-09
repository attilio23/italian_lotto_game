from classes.ticket import Ticket
from classes.print_output import PrintOutput


MN_QUANTITY = 1
MX_QUANTITY = 5


def start(tckt_nmbr):
  if not(tckt_nmbr):
    print("\n" + (PrintOutput.PrintLine("NO TICKETS WERE GENERATED")))
    quit()
  
  tickets = []
  
  for i in range (tckt_nmbr):
    tickets.append(Ticket())

  i = 1

  for ticket in tickets:
    print((PrintOutput.PrintLine("GENERATING THE TICKET " + str(i) + "...")) + "\n")
    nmbr_amount = ticket.SetNumbersPlayed()
    ticket.SetBillType(nmbr_amount)
    ticket.SetCity()
    i = i + 1

  if len(tickets) == 1:
    print((PrintOutput.PrintLine("YOUR TICKET:")) + "\n")
  else:
    print((PrintOutput.PrintLine("YOUR TICKETS:")) + "\n") 
  
  for ticket in tickets:
    print(ticket)


if __name__ == "__main__":
  print((PrintOutput.PrintLine("LOTTO TICKET GENERATOR")) + "\n")
  ticket_quantity = input("\nEnter the number of tickets you want to generate: (min: 1, max: 5, 0: exit)\n\n")
  
  while ticket_quantity < str(MN_QUANTITY - 1) or ticket_quantity > str(MX_QUANTITY) or len(ticket_quantity) != 1:
    print("\nThe input is invalid.")
    ticket_quantity = input("Enter the number of tickets you want to generate: (min: 1, max: 5, 0: exit)\n\n") 
  
  start(int(ticket_quantity))