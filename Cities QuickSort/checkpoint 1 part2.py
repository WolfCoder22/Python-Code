from cityclass import City

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
    
    
in_file.close()

#open cities out file and add to it
out_file=open("cities_out.txt", "w")

#for each city object in cities list, write that object to the list
for i in cities:
    out_file.write(str(i)+ "\n")
    
out_file.close()
    

    
    