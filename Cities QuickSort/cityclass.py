#class for city
class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code=country_code
        self.name=name
        self.region=region
        self.population=population
        self.latitude=latitude
        self.longitude=longitude
    
    def __str__(self):
        return self.name+","+str(self.population)+","+str(self.latitude)+","+str(self.longitude)

