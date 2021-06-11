class City():
    cities = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
    
    
    def __init__(self, city_name = ""):
        self.city_name = city_name    
    
    
    def __str__(self):
        return "%s" % (self.city_name)
    
    
    def IsCityValid(city_name):
        if city_name in City.cities:
            return True
        return False