# Italian Lotto Game  
This project is based on the Italian Lotto Game.  
It consists of three learning paths.  
For more information about the Lotto Game visit: https://www.sisal.it/lotto/come-si-gioca

## Learning path 3
This branch represents the third level of the project. The user can generate zero, one or more tickets. 
For each ticket generated, it is specified whether it is a 
winning ticket or a non-winning ticket (if a ticket is winning, the result is shown). 
For each winning ticket, the gross prize and the net prize are shown.

### Structure
* lotto_game.py:
The file from which to start the program.

* classes:
The folder that contains all the classes used in the program:
  
  * NumbersPlayed:
  
    It represents the set of numbers played for a specific ticket.
  
  * BillType:
  
    It represents the bill type for a specific ticket.
  
  * City:
       
    It represents the city for a specific ticket.
  
  * AmountPlayed:

    It represents the amount played for a specific ticket.

  * Ticket:
       
    It represents a ticket.
  
  * Extraction:
     
    It represents an extraction.
  
  * PrintOutput:

    It manages the printing of the output, the ticket and the extraction.
