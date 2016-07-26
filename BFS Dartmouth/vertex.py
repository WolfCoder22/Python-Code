#creates class for vertex
from cs1lib import *

class Vertex:
    #constructor method
    def __init__(self, name, x_position, y_position):
        #delcares instance variables
        self.name=name
        self.x=int(x_position)
        self.y=int(y_position)
        self.adjacent_list=[]

    #string method
    def __str__(self):
        #adds the names of adjacent vertices of a vertex to a string 
        string=""
        for i in self.adjacent_list:
            string=string+i.name+", "
        string=string[0:-2]
        
        return self.name+"; Location: "+str(self.x)+", "+str(self.y)+"; Adjacent vertices: "+string
    
    #method which draws the vertex based parameters r,g,b
    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        disable_stroke()
        enable_fill()
        enable_smoothing()
        draw_circle(self.x, self.y, 5)
    
    #method that draws an edge of the object and another object inputed as a parameter
    def draw_edge(self, vertex_object, r, g, b):
        enable_stroke()
        set_stroke_color(r,g,b)
        set_stroke_width(2)
        draw_line(vertex_object.x, vertex_object.y, self.x, self.y)
        
    #draw all adjacent edges to a object
    def draw_edges(self, r, g, b):
        enable_stroke()
        set_stroke_color(r,g,b)
        set_stroke_width(2)
        for i in self.adjacent_list:
            draw_line(i.x, i.y, self.x, self.y)
            
    #method which prints name of object       
    def print_name(self):
        enable_stroke()
        set_stroke_color(0,0,0)
        draw_text(self.name, self.x-5, self.y-10)
        
    #method to check if a point is on a vertex
    def in_box(self, x,y):
        return self.x-5<=x<=self.x+5 and self.y+5>=y>=self.y-5
        
        

        