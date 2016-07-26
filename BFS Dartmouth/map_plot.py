from cs1lib import *
from load_graph import *
from vertex import Vertex
from time import sleep
from bfs import bfs

WINDOW_WIDTH= 1012
WINDOW_HEIGHT=811
NAP= .02

#function that draws background consisting of map and graph
def draw_background(vertex_dictionary):
    
    #load image of dartmouth map and load it to window
    img=load_image("dartmouth_map.png")
    draw_image(img,0,0)
    
    #for every vertex object in the dictionary
    for key in vertex_dictionary:
        #draw an edge to all of it's adjacent vertices
        vertex_dictionary[key].draw_edges(0,0,0)
    for key in vertex_dictionary:
        #draw the vertex in green
        vertex_dictionary[key].draw_vertex(0,1,0)
        
        
def main():
    
    #creates vertex object dictionary from load graph function
    vertex_dictionary=load_graph("dartmouth_graph.txt")
    
    #initialize start and goal vertex variables
    start_vertex=None
    goal_vertex= None
    
    while not window_closed():
        
        #draw the background
        draw_background(vertex_dictionary)
        
        for key in vertex_dictionary:
            
            #if mouse clicks on a vertex make it the starting vertex
            if vertex_dictionary[key].in_box(mouse_x(), mouse_y()) and mouse_down() and start_vertex!=goal_vertex:
                start_vertex=vertex_dictionary[key]
               
                
            #if mouse hovers over another vertex make that the goal vertex
            if vertex_dictionary[key].in_box(mouse_x(), mouse_y()) and vertex_dictionary[key]!=start_vertex:
                goal_vertex=vertex_dictionary[key]
                
                
        
        #performs bfs for start and goal vertices once declared
        if start_vertex!= None and goal_vertex!=None:
            #pathway is list of vertices from goal to start vertex created from bfs
            pathway= bfs(start_vertex, goal_vertex)
             
            for i in range(len(pathway)):
                #draw each vertex in pathway
                pathway[i].draw_vertex(1,0,0)
                #draw each edge in pathway
                if i<len(pathway)-1:
                    pathway[i].draw_edge(pathway[i+1],1,0,0)  
        
        
        #update the window and nap
        request_redraw()
        sleep(NAP)
        
start_graphics(main, "Dartmouth Map",WINDOW_WIDTH, WINDOW_HEIGHT )
