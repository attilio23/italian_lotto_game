from classes.bill_type import BillType
from classes.print_helper import PrintHelper


class AmountPlayed():
    np_gross = {1 : [11.23], 2 : [5.61, 250.00], 3 : [3.74, 83.33, 4500.00], \
4 : [2.80, 41.66, 1125.00, 120000.00], 5 : [2.24, 25.00, 450.00, 24000.00, 6000000.00], \
6 : [1.87, 16.66, 225.00, 8000.00, 1000000.00], 7 : [1.60, 7.85, 11.90, 128.57, 3428.57, 285714.28], \
8 : [1.40, 8.92, 80.35, 1714.28, 107142.85], 9 : [1.24, 6.94, 53.57, 952.38, 47619.04], \
10 : [1.12, 5.55, 37.50, 571.42, 23809.52]}
    np_net = {1 : [10.33], 2 : [5.16, 230.00], 3 : [3.44, 76.66, 4140.00], \
4 : [2.57, 38.32, 1035.00, 110400.00], 5 : [2.06, 23.00, 414.00, 22080.00, 5520000.00], \
6 : [1.72, 15.32, 207.00, 7360.00, 920000.00], 7 : [1.47, 10.94, 118.28, 3154.28, 262857.13], \
8 : [1.28, 8.20, 73.92, 1577.13, 98571.42], 9 : [1.14, 6.38, 49.28, 876.18, 43809.51], \
10 : [1.03, 5.10, 34.50, 525.70, 21904.75]}
    

    def __init__(self, amount = ""):
        self.amount = amount

    
    def __str__(self):
        return "%s" % (self.amount)
    

    def is_amount_valid(self, amount):
        mn = 1.00
        mx = 200.00
        
        if not("," in amount):
            return False
        
        amount = amount.replace(",", ".")
        
        if amount[amount.find(".") + 1 :] != "50" and amount[amount.find(".") + 1 :] != "00":
            return False
        
        if len(amount[: amount.find(".")]) > 1 and amount[: amount.find(".")][0] == "0":
            return False 

        try:
            if mn <= float(amount) <= mx:
                amount = amount.replace(".", ",")
                self.amount = amount + " €"
                return True
            
            return False
        except ValueError:
            return False


    def calculate_prize(self, city, b_type, num_amount):
        amount = self.amount.replace(",", ".")
        amount = amount[: amount.find(" €")]

        if city == "Tutte":
            gross_prize = (float(amount) * AmountPlayed.np_gross[num_amount][BillType.tyId[b_type] - 1]) / 10
            net_prize = (float(amount) * AmountPlayed.np_net[num_amount][BillType.tyId[b_type] - 1]) / 10
        else:
            gross_prize = round(float(amount) * AmountPlayed.np_gross[num_amount][BillType.tyId[b_type] - 1], 2)
            net_prize = round(float(amount) * AmountPlayed.np_net[num_amount][BillType.tyId[b_type] - 1], 2)    
    
        gross_prize = "%.2f" % (gross_prize)
        net_prize = "%.2f" % (net_prize)
        gross_prize = gross_prize.replace(".", ",")
        net_prize = net_prize.replace(".", ",")
        return (PrintHelper.thousands_separator(gross_prize[: gross_prize.find(",")]) + gross_prize[gross_prize.find(",") :] + " €", \
PrintHelper.thousands_separator(net_prize[: net_prize.find(",")]) + net_prize[net_prize.find(",") :] + " €")