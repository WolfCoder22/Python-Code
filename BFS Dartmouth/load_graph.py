from vertex import Vertex

def load_graph(data_file_name):
    #creates library for vertex objects
    vertex_dictionary= {}   
    
    in_file=open(data_file_name)
    
    
    for line in in_file:
        #turns each line of vertex data to list
        line=line.strip()
        line=line.split(";")
        
        #creates sublist of x and y coordinates for each line 
        line[2]=line[2].strip()
        line[2]=line[2].split(",")
        
        #create vertex object with Name, x coordinate, and y coordinate
        new_vertex=Vertex(line[0],line[2][0], line[2][1])
        #adds that object the vertex dictionary
        vertex_dictionary[line[0]]=new_vertex
    
    in_file.close()
    
    in_file=open(data_file_name)
    
    for line in in_file:
        line=line.strip()
        line=line.split(";")
        
        #creates sublist of adjacent vertices of a vertex
        line[1]=line[1].split(",")
        
        
        #Adds adjacent vertex object references to adjacent_list instance variable
        for i in line[1]:
            i=i[1:] #gets rid of space in front of each adjacent vertex name
            vertex_dictionary[line[0]].adjacent_list.append(vertex_dictionary[i])
               
    in_file.close()
    #returns dictionary address
    return vertex_dictionary
        