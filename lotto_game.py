from classes.numbers_played import NumbersPlayed
from classes.bill_type import BillType
from classes.city import City
from classes.ticket import Ticket
from line_content import CentralContent
MN_QUANTITY = 1
MX_QUANTITY = 5
tickets = []
print(CentralContent("LOTTO TICKET GENERATOR", 112) + "\n")
ticket_quantiy = input("\nEnter the number of tickets you want to generate: (min: 1, max: 5, 0: exit)\n\n")
while ticket_quantiy < "0" or ticket_quantiy > "5" or len(ticket_quantiy) != 1:
  print("\nThe input is invalid.")
  ticket_quantiy = input("Enter the number of tickets you want to generate: (min: 1, max: 5, 0: exit)\n\n")    
ticket_quantiy = int(ticket_quantiy)
if not(ticket_quantiy):
  print("\nNO TICKETS WERE GENERATED.")
  quit()
for i in range(ticket_quantiy):
  print(CentralContent("GENERATING THE TICKET " + str(i + 1) + "...", 112) + "\n")
  number_amount = input("How many numbers do you want to play? (max 10 per bill)\n\n")
  while not(NumbersPlayed.NumAmountIsValid(number_amount)):
    print("\nThe input is invalid.")
    number_amount = input("How many numbers do you want to play? (max 10 per bill)\n\n")    
  number_amount = int(number_amount)
  bill_type = input("\nEnter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")
  while not(BillType.IsTypeValid(bill_type, number_amount)):
    print("\nThe input is invalid.")
    bill_type = input("Enter the type of bill:\nAmbata ---> At least one number must be played\n\
Ambo ---> At least two numbers must be played\nTerno ---> At least three numbers must be played\n\
Quaterna ---> At least four numbers must be played\nCinquina ---> At least five numbers must be played\n\n")    
  city = input("\nEnter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")
  while not(City.IsCityValid(city)):
    print("\nThe input is invalid.")
    city = input("Enter the city of the bill: (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia, Tutte)\n\n")
  numbers_played = NumbersPlayed()
  numbers_played.GenerateNumbers(number_amount)
  tickets.append(Ticket(bill_type, city, numbers_played.numbers))
if len(tickets) == 1:
  print(CentralContent("YOUR TICKET:", 112) + "\n")
else:
  print(CentralContent("YOUR TICKETS:", 112) + "\n") 
for ticket in tickets:
  print(ticket)