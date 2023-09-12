def adjacency_matrix(graph_str):
    """Returns the adjacency matrix of a string"""
    #First create a list of the items in the string
    iteration = 0
    directed = False
    weighted = False
    graph_list = []
    
    #Organises the string into list form
    empty_string = ''
    for item in graph_str:
        if item not in ('\n', ' ', ',', ''):
            empty_string += item
        else:
            graph_list.append(empty_string)
            empty_string = ''
    
    #Creates the number of lists in the matrix
    outer_list = [[] for i in range(int(graph_list[1]))] 
    
    #Iterates through the matrix, and fills it with 0, times the number of vertices.
    num_vertices = int(graph_list[1])
    for item in outer_list:
        count = num_vertices
        while count > 0:
            item.append(None)
            count -= 1
    #print(outer_list)
    #print(graph_list)
    #graph_list is the list with all elements we read in an array form.
    #Checks if the graph is directed, and weighted.
    
    if graph_list[0] == 'D':
        directed = True
    if len(graph_list) > 2:
        if graph_list[2] == 'W':
            weighted = True    
            
    #print(graph_list)
    #print(outer_list)
    #print(f"directed = {directed}")
    #print(f"weighted = {weighted}")
    #Create a command for all situations
    
    if weighted == False:
        if directed == True:
            #Start by ignoring the first line
            iteration = 2
            while iteration < (len(graph_list) - 1):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                outer_list[vertex1][vertex2] = 1
                iteration += 2

        else:
            iteration = 2
            while iteration < (len(graph_list) - 1):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                outer_list[vertex1][vertex2] = 1
                outer_list[vertex2][vertex1] = 1
                iteration += 2
        
        #Use a while loop to change Nones into 0s
        for row in outer_list:
            iterate = 0
            while iterate < len(outer_list):
                if row[iterate] == None:
                    row[iterate] = 0
                iterate += 1
                
                
            
        
        
    else:
        #Weighted is True:
        if directed == True:
            iteration = 3
            while iteration < (len(graph_list) - 2):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                weight = int(graph_list[iteration + 2])
                # print(vertex1, vertex2, weight)
                outer_list[vertex1][vertex2] = weight
                iteration += 3
        #If the tree is undirected
        else:
            iteration = 3
            while iteration < (len(graph_list) - 2):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                weight = int(graph_list[iteration + 2])
                # print(vertex1, vertex2, weight)
                outer_list[vertex1][vertex2] = weight
                outer_list[vertex2][vertex1] = weight
                iteration += 3
                
    return outer_list, len(graph_str)


def bubbles(physical_contact_info):
    """returns a list of bubbles, with each element being a set"""
    outer_list, length = adjacency_matrix(physical_contact_info)
    #print(length)
    #print(outer_list)
    iterable = 0
    iterable2 = 0
    count = 0
    #Empty_list is the vertices.
    empty_list = []
    empty_answer = []
    #Case there isn't any edges.
    if length < 5:
        for item in outer_list:
            empty_answer.append([count])
            count += 1
        return empty_answer
    
    #print(outer_list)
    for index in range(len(outer_list)):
        set_a = set()
        iterable = 0
        set_a.add(index)
        lists = outer_list[index]
        while iterable < len(lists):
            iterable2 = 0
            if lists[iterable] == 1:
                set_a.add(iterable)
            iterable += 1
            intersects = False
        
        
        if len(empty_list) == 0:
            set_a.add(count)
            empty_list.append(set_a)
            #print(empty_list)
        
        
        else:
            while iterable2 < len(empty_list):
                set_b = empty_list[iterable2]
                #print(f"looking for {set_b} intersection {set_a}")
                if len(set_b.intersection(set_a)) == 0:
                    iterable2 += 1
                    #print("there is no intersection")
                else:
                    intersects = True
                    empty_list[iterable2] = set_a.union(set_b)
                    iterable2 += 1
            if intersects == False:
                empty_list.append(set_a)
            #print(empty_list)
            #print('')
        count += 1
    return empty_list
    


physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)) == [[0, 1]])


physical_contact_info = """\
U 2
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)) == [[0], [1]])


physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)) == [[0], [1, 2, 3, 4, 5, 6]])

physical_contact_info = """\
U 0
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)) == [])

physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)) == [[0]])


physical_contact_info = """\
U 4
2 1
"""

print(sorted(sorted(bubble)
             for bubble in bubbles(physical_contact_info)) == [[0], [1, 2], [3]])

physical_contact_info = """\
U 7
1 4
2 0
4 6
5 3
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)) == [[0, 2], [1, 4, 6], [3, 5]])