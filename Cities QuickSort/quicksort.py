#Alex Wolf
#Quicksort Lab

  

#functions that swaps two elements in a list based off indexs
def swap(the_list,x,y):
    temp=the_list[x]
    the_list[x]=the_list[y]
    the_list[y]=temp

#partition function that partitions a list
def partition(the_list, p, r, compare_func):
    pivot =the_list[r]  #sets pivot to last element of list
    i=p-1
    j=p
    while j<r:
        if compare_func(the_list[j],pivot):
            i+=1
            swap(the_list, j,i) #swaps elements at index i and j if j is less than pivot
        j+=1
        
    #swaps pivot with index i+1, and returns that index
    swap(the_list,r,i+1)
    return i+1 

#recursive quicksort function
def quicksort(the_list, p, r, compare_func):
    if r>p:
        #q= index of the list which list was partitioned 
        q= partition(the_list, p, r, compare_func)
        #recursively call quicksort on the two sublist left and right of q
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)
    
#function that sorts a list based off a specific comparison
def sort(the_list, compare_func):
    quicksort(the_list,0,len(the_list)-1, compare_func)
    

    
            
        
        