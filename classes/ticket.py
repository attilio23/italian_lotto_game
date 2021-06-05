from classes.bill_type import BillType
from classes.numbers_played import NumbersPlayed
from classes.city import City
from line_content import CentralContent, LateralContent
class Ticket():
    def __init__(self, type = "", city_name = "", numbers = "",):
        self.b_t = BillType(type)
        self.n_p = NumbersPlayed(numbers)
        self.c = City(city_name)    
    def __str__(self):
        width = 45                                                                                         
        return "╔═════════════════════════════════════════════╗\n\
║ ┌──┐   ┌─────┐┌─────────┐┌─────────┐┌─────┐ ║\n\
║ │  │   │ ┌─┐ │└──┐   ┌──┘└──┐   ┌──┘│ ┌─┐ │ ║\n\
║ │  │   │ │ │ │   │   │      │   │   │ │ │ │ ║\n\
║ │  └──┐│ └─┘ │   │   │      │   │   │ └─┘ │ ║\n\
║ └─────┘└─────┘   └───┘      └───┘   └─────┘ ║\n\
╠═════════════════════════════════════════════╣\n\
║" + LateralContent(" CITY: " + self.c.city_name, width) + "║\n\
║" + CentralContent("_____________________", width) + "║\n\
║                                             ║\n\
║" + LateralContent(" TYPE: " + self.b_t.type, width) + "║\n\
║" + CentralContent("_____________________", width) + "║\n\
║                                             ║\n\
║" + CentralContent(self.n_p.numbers, width) + "║\n\
║                                             ║\n\
╚═════════════════════════════════════════════╝"