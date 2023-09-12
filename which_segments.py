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
                
                
    return outer_list


def which_segments(city_map):
    """Stuff"""
    current_min = None
    #Parses in the adjacency matrix
    matrix = adjacency_matrix(city_map)
    print(matrix)
    
    #Create a cost and visited list
    costs = []
    visited = []
    completed_example = []
    for item in range(len(matrix)):
        costs.append(float('inf'))
        visited.append('U')
        completed_example.append('V')
    #If the costs isn't empty, change starting vertex cost to 0
    if len(costs) > 0:
        costs[0] = 0
    
    #We're staring on Node 0, so change visited:
    if len(visited) > 0:
        visited[0] = 'V'
    #Find the next vertex with the cheapest cost
    current_vertex = 0      
    
    
    print(completed_example)
    while visited != completed_example:
        
        index = 0
        index2 = 0
        
        #Iterates through the matrix
        while index < len(matrix):
            #Iterates through the matrix nodes
            while index2 < len(matrix[index]):
                #If the node is not visiting itself, and has a valid path to another:
                if matrix[index][index2] != None:
                    value = matrix[index][index2]
                    #If the visit value is less than the current cost:
                    if (value < costs[index2]):
                        costs[index2] = matrix[index][index2]
                index2 += 1
            index += 1
        print(index2)
        print(f"Current vertex is: {current_vertex}")
            
        index, index2 = 0, 0
        #Now we visit the next node with the lowest value:
        
        #Creates a minimum to surpass
        if current_min == None:
            current_min = float('inf')
        
        #Saves the place of the vertex with the lowest value
        saved_vertex = None
        
        #Checks the minimum cost's vertex placement.
        while index < len(visited):
            #If the vertex has not been visited
            if visited[index] != 'V' and costs[index] < current_min:
                current_min = costs[index]
                saved_vertex = index
            index += 1
 
        #Redefines the vertex we are currently on
        current_vertex = saved_vertex
        print(current_vertex)
    
        #Changes the visited array
        visited[current_vertex] = 'V'
        print(visited)
    

city_map = """\
U 4 W
0 1 1
2 1 2
2 0 4
3 1 3
"""

print((which_segments(city_map)))