import datetime


class PrintOutput():
    ta_width_1 = 45
    ta_width_2 = 93
    ta_width_3 = 20
    te_width = 112
    separator_length = 21
    
    
    def PrintTableLine(width, content = ""):
        return "║" + content.center(width) + "║"
    

    def PrintLine(content = ""):
        return content.center(PrintOutput.te_width)


    def OpenTable(width):
        return "╔" + ("═" * width) + "╗" + "\n" + PrintOutput.PrintTableLine(width)


    def CloseTable(width):
        return PrintOutput.PrintTableLine(width) + "\n" + "╚" + ("═" * width) + "╝"


    def CloseOpenTable(width):
        return PrintOutput.PrintTableLine(width) + "\n" + "╠" + ("═" * width) + "╣" + "\n" + PrintOutput.PrintTableLine(width)


    def PrintSeparator(width):
        return PrintOutput.PrintTableLine(width) + "\n" + "" + PrintOutput.PrintTableLine(width, "_" * PrintOutput.separator_length) + "\n" + PrintOutput.PrintTableLine(width)

    
    def PrintToLeft1(width, content = ""):    
        return "║ " + content + (" " * ((width - 1) - len(content))) + "║"
    

    def PrintToLeft2(width, content = ""):    
        return content + (" " * ((width - 1) - len(content))) 
    
    
    def PrintTicket(city_name, type, numbers):
        s_ticket = ""
        s_lotto = ["┌──┐   ┌─────┐┌─────────┐┌─────────┐┌─────┐", \
                   "│  │   │ ┌─┐ │└──┐   ┌──┘└──┐   ┌──┘│ ┌─┐ │", \
                   "│  │   │ │ │ │   │   │      │   │   │ │ │ │", \
                   "│  └──┐│ └─┘ │   │   │      │   │   │ └─┘ │", \
                   "└─────┘└─────┘   └───┘      └───┘   └─────┘"]
        ticket_features = ["CITY: " + city_name, "TYPE: " + type]
        s_ticket = s_ticket + PrintOutput.OpenTable(PrintOutput.ta_width_1) + "\n"
        
        for line in s_lotto:
            s_ticket = s_ticket + PrintOutput.PrintTableLine(PrintOutput.ta_width_1, line) + "\n"
        
        s_ticket = s_ticket + PrintOutput.CloseOpenTable(PrintOutput.ta_width_1) + "\n"
        i = 0
        s_ticket = s_ticket + PrintOutput.PrintToLeft1(PrintOutput.ta_width_1, ticket_features[i]) + "\n" 
        s_ticket = s_ticket + PrintOutput.PrintSeparator(PrintOutput.ta_width_1) + "\n"
        i = i + 1
        
        while i < len(ticket_features):
            s_ticket = s_ticket + PrintOutput.PrintToLeft1(PrintOutput.ta_width_1, ticket_features[i]) + "\n"
            s_ticket = s_ticket + PrintOutput.PrintSeparator(PrintOutput.ta_width_1) + "\n"
            i = i + 1

        s_ticket = s_ticket + PrintOutput.PrintTableLine(PrintOutput.ta_width_1, numbers) + "\n"
        s_ticket = s_ticket + PrintOutput.CloseTable(PrintOutput.ta_width_1)
        return s_ticket


    def PrintExtraction(wheels):
        s_extraction = ""
        s_lotto = ["┌──┐   ┌─────┐┌─────────┐┌─────────┐┌─────┐", \
                   "│  │   │ ┌─┐ │└──┐   ┌──┘└──┐   ┌──┘│ ┌─┐ │", \
                   "│  │   │ │ │ │   │   │      │   │   │ │ │ │", \
                   "│  └──┐│ └─┘ │   │   │      │   │   │ └─┘ │", \
                   "└─────┘└─────┘   └───┘      └───┘   └─────┘"]  
        i = datetime.datetime.now()
        date = "%02d/%02d/%4d" % (i.day, i.month, i.year)
        extraction_information = ["EXTRACTION OF", date]
        cities = list(wheels.keys())   
        s_extraction = s_extraction + PrintOutput.OpenTable(PrintOutput.ta_width_2) + "\n" 
        
        for line in s_lotto:
            s_extraction = s_extraction + PrintOutput.PrintTableLine(PrintOutput.ta_width_2, line) + "\n"

        s_extraction = s_extraction + PrintOutput.CloseOpenTable(PrintOutput.ta_width_2) + "\n"
        
        for line in extraction_information:
            s_extraction = s_extraction + PrintOutput.PrintTableLine(PrintOutput.ta_width_2, line) + "\n"
        
        s_extraction = s_extraction + PrintOutput.CloseOpenTable(PrintOutput.ta_width_2) + "\n"
        delimeter = " "
        s_extraction = s_extraction + PrintOutput.PrintTableLine(PrintOutput.ta_width_2, (PrintOutput.PrintToLeft2(PrintOutput.ta_width_3, cities[0].upper())) + delimeter.join(wheels[cities[0]])) + "\n"
        
        for i in range(1, len(cities)):
            s_extraction = s_extraction + PrintOutput.PrintTableLine(PrintOutput.ta_width_2) + "\n"
            s_extraction = s_extraction + PrintOutput.PrintTableLine(PrintOutput.ta_width_2, (PrintOutput.PrintToLeft2(PrintOutput.ta_width_3, cities[i].upper())) + delimeter.join(wheels[cities[i]])) + "\n"
        
        s_extraction = s_extraction + PrintOutput.CloseTable(PrintOutput.ta_width_2)
        return s_extraction