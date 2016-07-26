from time import sleep
from cs1lib import *
from cityclass import City
from sort_cities import *
from quicksort import sort
from random import uniform

WINDOW_HEIGHT=360
WINDOW_WIDTH=720
NAP=.3

def main():
    #load map image for the window
    img=load_image("world.png")
    draw_image(img, 0, 0)
    
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
        
    #close the file
    in_file.close()
        
    #sort cities of population
    sort(cities,compare_population)
        
    #delete all but 50 most populated cities in the list
    del cities[50:]
    
    #draw each city in the cities list
    for city in cities:
        #draws city name
        enable_stroke()
        set_stroke_color(0,0,0)
        draw_text(city.name, WINDOW_WIDTH/2+float(city.longitude)*2-13, WINDOW_HEIGHT/2+float(city.latitude)*2+10)
        
        
        disable_stroke()
        r=uniform(0,1)
        g=uniform(0,1)
        b=uniform(0,1)
        set_fill_color(r,g,b)
        enable_smoothing()
        #draws city off instance variable longitudes and latitude
        draw_circle(WINDOW_WIDTH/2+float(city.longitude)*2,WINDOW_HEIGHT/2+float(city.latitude)*2,5)
        
        request_redraw()
        sleep(0)
        
        #redraws over city name in white to hide the name
        enable_stroke()
        set_stroke_color(1,1,1)
        draw_text(city.name, WINDOW_WIDTH/2+float(city.longitude)*2-13, WINDOW_HEIGHT/2+float(city.latitude)*2+10)
        request_redraw()
        

start_graphics(main, "Locations of 50 most populated cities", WINDOW_WIDTH, WINDOW_HEIGHT, flipped_y = True)
        
        
        
    