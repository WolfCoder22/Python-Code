from cs1lib import *
from load_graph import *
from vertex import Vertex
from collections import deque


#perform a breadth first search for an undirected unwieghted graph
def bfs(s,g):
    
    #create an empty list to contain the pathway of vertex objects from goal vertex to start vertex
    pathway=[]
    
    #create dictionary of back_pointers
    back_pointer_dict={}
    
    #initializes start vertex to have no back pointer
    back_pointer_dict[s]=None
    
    #create deque for bfs and append start vertex
    q =deque()
    q.append(s)
    
    #while loop which performs bfs and creates a dictionary with the  back-pointers of vertices. 
    while len(q) !=0 and not g in back_pointer_dict:
        #return value then pop the first element in a list
        x=q.popleft()
        
        #for all adjacent vertices of vertex just popped
        for vertex in x.adjacent_list:
            #if not already in back_pointer_dict
            if not vertex in back_pointer_dict:
                #create dictionary entry with the key a vertex and the value it's back-ointer
                back_pointer_dict[vertex]=x
                #append vertex to deque
                q.append(vertex)
    
    #set current vertex to goal vertex
    current_vertex= g
    
    #loop that runs until start vertex reached
    while back_pointer_dict[current_vertex]!=None:
        #append current vertex to pathway list
        pathway.append(current_vertex)
        #set current vertex to it's back pointer
        current_vertex=back_pointer_dict[current_vertex]
    
    #append the start vertex to pathway list
    pathway.append(current_vertex)
    
    #return the pathway list
    return pathway
                
    
