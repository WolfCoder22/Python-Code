from string import lower
from quicksort import*
from cityclass import City


#compare functions that compare data off of various criteria
def compare_population(city1, city2):
    return city1.population>=city2.population

def compare_city_name(city1, city2):
    return lower(city1.name)<=lower(city2.name)

def compare_latitude(city1, city2):
    return city1.latitude<=city2.latitude


#opens world_cities.text
in_file= open("world_cities.txt")

cities=[] #create empty list of cities
for line in in_file:
    
    #take away whitespace and make each line a list
    line=line.strip()
    line=line.split(",")
    
    #change some string variables in the list to other data types
    line[3]=int(line[3])
    line[4]=float(line[4])
    line[5]=float(line[5])
    
    #create an object from data in each line and add it to the cities list
    city=City(line[0],line[1],line[2],line[3],line[4],line[5])
    cities.append(city)
    
in_file.close()#closes file


#sort world cities based off population
sort(cities, compare_population)
#write sorted list into cities population text
out_file=open("cities_population.txt", "w")
for i in cities:
    out_file.write(str(i)+ "\n")
out_file.close()

#sort world cities based off name
sort(cities, compare_city_name)
#write sorted list into cities alpha text
out_file=open("cities_alpha.txt", "w")
for i in cities:
    out_file.write(str(i)+ "\n")  
out_file.close()

#sort world cities based off latitude
sort(cities, compare_latitude)
#write sorted list into cities latitude text
out_file=open("cities_latitude.txt", "w")
for i in cities:
    out_file.write(str(i)+ "\n")  
out_file.close()
    
