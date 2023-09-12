def adjacency_list(graph_str):
    """Takes textual string of graph and turns into list of lists"""
    iteration = 0
    directed = False
    weighted = False
    graph_list = []
    empty_string = ''
    for item in graph_str:
        if item not in ('\n', ' '):
            empty_string += item
        else:
            graph_list.append(empty_string)
            empty_string = ''
    #print(graph_list)
    
    outer_list = [[] for i in range(int(graph_list[1]))]
    
    
    #graph_list is the list with all elements we read in an array form.
    
    if graph_list[0] == 'D':
        directed = True
    if len(graph_list) > 2:
        if graph_list[2] == 'W':
            weighted = True   
    #print(len(graph_str))
    #print(f"Weighted = {weighted}")
    #print(f"Directed = {directed}")
    #print(f"Number of vertices is: {graph_list[1]}")
    #Case that the tree is unweighted, tuples 2nd element is false
    if weighted == False:
        if directed == True:
            #Start by ignoring the first line
            iteration = 2
            while iteration < (len(graph_list) - 1):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                outer_list[vertex1].append((vertex2, None))
                iteration += 2
                
        else:
            iteration = 2
            while iteration < (len(graph_list) - 1):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                outer_list[vertex1].append((vertex2, None))
                outer_list[vertex2].append((vertex1, None))
                iteration += 2
    #Case that the tree is weighted:
    else:
        if directed == True:
            iteration = 3
            while iteration < (len(graph_list) - 2):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                weight = int(graph_list[iteration + 2])
                # print(vertex1, vertex2, weight)
                outer_list[vertex1].append((vertex2, weight))
                iteration += 3
        #If the tree is undirected
        else:
            iteration = 3
            while iteration < (len(graph_list) - 2):
                vertex1 = int(graph_list[iteration])
                vertex2 = int(graph_list[iteration + 1])
                weight = int(graph_list[iteration + 2])
                # print(vertex1, vertex2, weight)
                outer_list[vertex1].append((vertex2, weight))
                outer_list[vertex2].append((vertex1, weight))
                iteration += 3
    
    return outer_list

def distance_matrix(adj_list):
    """Returns a distance input for Ffloyd's algorithm"""
    #print(adj_list)
    #Start by creating an empty list for inputs
    empty_list = [[float('inf') for item in adj_list] for item in adj_list]
    #So now we have an array of lists in which all have length 'inf' in them.
    
    #We now need to update the distances
    #print(empty_list)
    
    #Creates some indexes for while loops
    index, index2, index3 = 0, 0, 0
    
    #We now need to iterate through the adj_list
    while index < len(adj_list):
        #Resets the index 2 so we can reiterate through the tuples
        index2 = 0
        while index2 < len(adj_list[index]):
            #Creates a variable for the tuples within the list index
            tuples = adj_list[index][index2]
            
            #Updates the empty_list array to the weight
            empty_list[index][(tuples[0])] = tuples[1]
            #print(tuples)
            index2 += 1
        
        #Updates the distance from a node to itself, to 1.    
        empty_list[index][index] = 0
        index += 1
    
    return empty_list
    


    

def floyd(distance):
    """Returns a matrix after the floyd algorithm has been run"""
    #Follow psuedocode format where we iterate i, then j, then k
    i = 0
    while i < len(distance):
        j = 0
        while j < len(distance):
            k = 0
            while k < len(distance):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                k += 1
            j += 1
        i += 1
    
    return distance
    
graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_list = adjacency_list(graph_str)
dist_matrix = distance_matrix(adj_list)
print("Initial distance matrix:", dist_matrix)
dist_matrix = floyd(dist_matrix)
print("Shortest path distances:", dist_matrix)

import pprint

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))