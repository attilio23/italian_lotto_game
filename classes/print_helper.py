class PrintHelper():
    te_width = 112
    ta_width = 45
    separator_length = 21
    
    
    def print_table_line(content = ""):
        return "║" + content.center(PrintHelper.ta_width) + "║"
    

    def print_line(content = ""):
        return content.center(PrintHelper.te_width)


    def open_table():
        return "╔" + ("═" * PrintHelper.ta_width) + "╗" + "\n" + PrintHelper.print_table_line()


    def close_table():
        return PrintHelper.print_table_line() + "\n" + "╚" + ("═" * PrintHelper.ta_width) + "╝"


    def close_open_table():
        return PrintHelper.print_table_line() + "\n" + "╠" + ("═" * PrintHelper.ta_width) + "╣" + "\n" + PrintHelper.print_table_line()


    def print_separator():
        return PrintHelper.print_table_line() + "\n" + "" + PrintHelper.print_table_line("_" * PrintHelper.separator_length) + "\n" + PrintHelper.print_table_line()

    
    def print_to_left(content = ""):
        return "║ " + content + (" " * ((PrintHelper.ta_width - 1) - len(content))) + "║"

    
    def print_ticket(city_name, type, numbers):
        s_ticket = ""
        s_lotto = ["┌──┐   ┌─────┐┌─────────┐┌─────────┐┌─────┐", \
                   "│  │   │ ┌─┐ │└──┐   ┌──┘└──┐   ┌──┘│ ┌─┐ │", \
                   "│  │   │ │ │ │   │   │      │   │   │ │ │ │", \
                   "│  └──┐│ └─┘ │   │   │      │   │   │ └─┘ │", \
                   "└─────┘└─────┘   └───┘      └───┘   └─────┘"]
        ticket_features = ["CITY: " + city_name, "TYPE: " + type]
        s_ticket = s_ticket + PrintHelper.open_table() + "\n"
        
        for line in s_lotto:
            s_ticket = s_ticket + PrintHelper.print_table_line(line) + "\n"
        
        s_ticket = s_ticket + PrintHelper.close_open_table() + "\n"
        i = 0
        s_ticket = s_ticket + PrintHelper.print_to_left(ticket_features[i]) + "\n" 
        s_ticket = s_ticket + PrintHelper.print_separator() + "\n"
        i = i + 1
        
        while i < len(ticket_features):
            s_ticket = s_ticket + PrintHelper.print_to_left(ticket_features[i]) + "\n"
            s_ticket = s_ticket + PrintHelper.print_separator() + "\n"
            i = i + 1
        
        s_ticket = s_ticket + PrintHelper.print_table_line(numbers) + "\n"
        s_ticket = s_ticket + PrintHelper.close_table()
        return s_ticket