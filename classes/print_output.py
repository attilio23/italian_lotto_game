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