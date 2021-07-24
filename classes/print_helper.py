import datetime


class PrintHelper():
    ta_width_1 = 45
    ta_width_2 = 93
    ta_width_3 = 20
    te_width = 112
    separator_length = 21
    

    @staticmethod    
    def print_table_line(width, content = ""):
        return "║" + content.center(width) + "║"
    

    @staticmethod
    def print_line(content = ""):
        return content.center(PrintHelper.te_width)


    @staticmethod
    def open_table(width):
        return "╔" + ("═" * width) + "╗" + "\n" + PrintHelper.print_table_line(width)


    @staticmethod
    def close_table(width):
        return PrintHelper.print_table_line(width) + "\n" + "╚" + ("═" * width) + "╝"


    @staticmethod 
    def close_open_table(width):
        return PrintHelper.print_table_line(width) + "\n" + "╠" + ("═" * width) + "╣" + "\n" + PrintHelper.print_table_line(width)


    @staticmethod
    def print_separator(width):
        return PrintHelper.print_table_line(width) + "\n" + "" + PrintHelper.print_table_line(width, "_" * PrintHelper.separator_length) + "\n" + PrintHelper.print_table_line(width)

    
    @staticmethod
    def print_to_left_1(width, content = ""):
        return "║ " + content + (" " * ((width - 1) - len(content))) + "║"

    
    @staticmethod
    def print_to_left_2(width, content = ""):    
        return content + (" " * ((width - 1) - len(content)))

    
    @staticmethod
    def print_ticket(city_name, type, numbers):
        s_ticket = ""
        s_lotto = ["┌──┐   ┌─────┐┌─────────┐┌─────────┐┌─────┐", \
                   "│  │   │ ┌─┐ │└──┐   ┌──┘└──┐   ┌──┘│ ┌─┐ │", \
                   "│  │   │ │ │ │   │   │      │   │   │ │ │ │", \
                   "│  └──┐│ └─┘ │   │   │      │   │   │ └─┘ │", \
                   "└─────┘└─────┘   └───┘      └───┘   └─────┘"]
        ticket_features = ["CITY: " + city_name, "TYPE: " + type]
        s_ticket = s_ticket + PrintHelper.open_table(PrintHelper.ta_width_1) + "\n"
        
        for line in s_lotto:
            s_ticket = s_ticket + PrintHelper.print_table_line(PrintHelper.ta_width_1, line) + "\n"
        
        s_ticket = s_ticket + PrintHelper.close_open_table(PrintHelper.ta_width_1) + "\n"
        i = 0
        s_ticket = s_ticket + PrintHelper.print_to_left_1(PrintHelper.ta_width_1, ticket_features[i]) + "\n" 
        s_ticket = s_ticket + PrintHelper.print_separator(PrintHelper.ta_width_1) + "\n"
        i = i + 1
        
        while i < len(ticket_features):
            s_ticket = s_ticket + PrintHelper.print_to_left_1(PrintHelper.ta_width_1, ticket_features[i]) + "\n"
            s_ticket = s_ticket + PrintHelper.print_separator(PrintHelper.ta_width_1) + "\n"
            i = i + 1
        
        s_ticket = s_ticket + PrintHelper.print_table_line(PrintHelper.ta_width_1, numbers) + "\n"
        s_ticket = s_ticket + PrintHelper.close_table(PrintHelper.ta_width_1)
        return s_ticket


    @staticmethod
    def print_extraction(wheels):
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
        s_extraction = s_extraction + PrintHelper.open_table(PrintHelper.ta_width_2) + "\n" 
        
        for line in s_lotto:
            s_extraction = s_extraction + PrintHelper.print_table_line(PrintHelper.ta_width_2, line) + "\n"

        s_extraction = s_extraction + PrintHelper.close_open_table(PrintHelper.ta_width_2) + "\n"
        
        for line in extraction_information:
            s_extraction = s_extraction + PrintHelper.print_table_line(PrintHelper.ta_width_2, line) + "\n"
        
        s_extraction = s_extraction + PrintHelper.close_open_table(PrintHelper.ta_width_2) + "\n"
        delimeter = " "
        s_extraction = s_extraction + PrintHelper.print_table_line(PrintHelper.ta_width_2, (PrintHelper.print_to_left_2(PrintHelper.ta_width_3, cities[0].upper())) + delimeter.join(wheels[cities[0]])) + "\n"
        
        for i in range(1, len(cities)):
            s_extraction = s_extraction + PrintHelper.print_table_line(PrintHelper.ta_width_2) + "\n"
            s_extraction = s_extraction + PrintHelper.print_table_line(PrintHelper.ta_width_2, (PrintHelper.print_to_left_2(PrintHelper.ta_width_3, cities[i].upper())) + delimeter.join(wheels[cities[i]])) + "\n"
        
        s_extraction = s_extraction + PrintHelper.close_table(PrintHelper.ta_width_2)
        return s_extraction