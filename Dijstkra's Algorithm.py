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



def dijkstra(adj_list, start):
    """Implements dijkstras algorithm"""
    
    def next_vertex(in_tree, distance):
        """Helper function to gain the next vertex to
        be used in Prim's and Dijkstra's algorithm"""
        possible_next = [] # Array to hold possible choices for next vertex
        next_vert = None # Initializing next vertex to None
        for index, vertex in enumerate(in_tree): # Looping over vertices in tree
            if not vertex:
                possible_next.append(index) # Vertex is not in tree so is considered for next vertex
        min_weight = distance[possible_next[0]] # Setting initial min weight
        next_vert = possible_next[0]
        for i in possible_next: # Looping over possible next vertices
            weight = distance[i] # Getting weight of current vertex
            if weight < min_weight: # Checking if current vertex has small weight than min weight
                min_weight = weight
                next_vert = i
        return next_vert # Returning next vertex
    
    len_adj = len(adj_list)
    in_tree = [False] * len_adj
    distance = [float('inf')] * len_adj
    parent = [None] * len_adj
    distance[start] = 0
    
    no_possible_vertex = []
    
    while not all(in_tree):
        next_vert = next_vertex(in_tree, distance)
        if next_vert == float('inf'):
            break
        in_tree[next_vert] = True
        for vertex, weight in adj_list[next_vert]:
            test = distance[next_vert] + weight
            if not in_tree[vertex] and test < distance[vertex]:
                distance[vertex] = test
                parent[vertex] = next_vert
    return parent, distance

def next_vertex(in_tree, distance):
    """Checks for the next vertex in the minimum spanning tree"""
    #Create a variable for the minimum distance:
    min_distance = float('inf')
    
    for i in range(len(in_tree)):
        #Checks if the item is not already in the tree somewhere
        if in_tree[i] == False:
            if distance[i] < min_distance:
                min_distance = distance[i]
                index = i
    
    #If the remaining distances are all infinite, get the first numerical instance
    if min_distance == inf:
        for i in range(len(in_tree)):
            #Checks if the item is not already in the tree somewhere
            if in_tree[i] == False:
                index = i
                return index    

    return index

from math import inf
in_tree = [False, True, True, False, False]
distance = [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance))

in_tree = [False, False, False]
distance = [float('inf'), 0, float('inf')]
print(next_vertex(in_tree, distance))

from math import inf
in_tree = [True, True, True, False, True]
distance = [inf, 0, inf, inf, inf]
print(next_vertex(in_tree, distance))
            
