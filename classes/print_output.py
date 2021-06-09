class PrintOutput():
    te_width = 112
    ta_width = 45
    separator_length = 21
    
    
    def PrintTableLine(content = ""):
        return "║" + content.center(PrintOutput.ta_width) + "║"
    

    def PrintLine(content = ""):
        return content.center(PrintOutput.te_width)


    def OpenTable():
        return "╔" + ("═" * PrintOutput.ta_width) + "╗" + "\n" + PrintOutput.PrintTableLine()


    def CloseTable():
        return PrintOutput.PrintTableLine() + "\n" + "╚" + ("═" * PrintOutput.ta_width) + "╝"


    def CloseOpenTable():
        return PrintOutput.PrintTableLine() + "\n" + "╠" + ("═" * PrintOutput.ta_width) + "╣" + "\n" + PrintOutput.PrintTableLine()


    def PrintSeparator():
        return PrintOutput.PrintTableLine() + "\n" + "" + PrintOutput.PrintTableLine("_" * PrintOutput.separator_length) + "\n" + PrintOutput.PrintTableLine()

    
    def PrintToLeft(content = ""):
        return "║ " + content + (" " * ((PrintOutput.ta_width - 1) - len(content))) + "║"

    
    def PrintTicket(city_name, type, numbers):
        s_ticket = ""
        s_lotto = ["┌──┐   ┌─────┐┌─────────┐┌─────────┐┌─────┐", \
                   "│  │   │ ┌─┐ │└──┐   ┌──┘└──┐   ┌──┘│ ┌─┐ │", \
                   "│  │   │ │ │ │   │   │      │   │   │ │ │ │", \
                   "│  └──┐│ └─┘ │   │   │      │   │   │ └─┘ │", \
                   "└─────┘└─────┘   └───┘      └───┘   └─────┘"]
        ticket_features = ["CITY: " + city_name, "TYPE: " + type]
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
        
        s_ticket = s_ticket + PrintOutput.PrintTableLine(numbers) + "\n"
        s_ticket = s_ticket + PrintOutput.CloseTable()
        return s_ticket