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
        if item not in ('\n', ' ', ',', '', '\\', ''):
            empty_string += item
        else:
            graph_list.append(empty_string)
            empty_string = ''
    
    #print(graph_list)
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
                
                
    return outer_list, num_vertices

def bfs_tree(adj_list, start):
    # number of vertices in the adjacency list of the graph.
    V = len(adj_list)

    # Initialise parent and visited arrays[].
    parent = [None] * V
    visited = [False] * V

    visited[start] = True
    queue = []
    queue.append(start)
    while len(queue) != 0:
        node_u = queue.pop(0)
        neighbours = adj_list[node_u]
        for node_v, weight in neighbours:
            if visited[node_v] is False:
                visited[node_v] = True
                parent[node_v] = node_u
                queue.append(node_v)
    return parent





def build_order(dependencies):
    """Takes an input of a directed graph, and builds it in a valid order"""
    outer_list, vertices = adjacency_matrix(dependencies)
    #print(outer_list)
    num_list = []
    for item in list(range(vertices)):
        num_list.append(0)
    answer = []
    
    index = 0
    
    for lists in outer_list:
        index = 0
        while index < len(lists):
            if lists[index] == 1:
                num_list[index] += 1
            index += 1
            
            
    #Calculate priorities and append accordingly
    index = 0
    index2 = 0
    empt = 0
    while index < len(num_list):
        index2 = 0
        while index2 < len(num_list):
            if num_list[index2] == index:
                parent = bfs_tree(adjacency_list(dependencies), index2)
                empt = 0
                for item in parent:
                    if item != None:
                        empt += 1
                num_list[index2] = empt            
            index2 += 1
        index += 1
        
    #Now print it in order
    index = 0
    index2 = 0
    while index < len(num_list):
        index2 = 0
        while index2 < len(num_list):
            if num_list[index2] == index:
                answer.append(index2)
            index2 += 1
        index += 1
    
    answer.reverse()
    return answer
    
dependencies = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""
print(build_order(dependencies))

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))
    
dependencies = """\
D 3
1 2
0 2
"""

print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])    

dependencies = """\
D 2
0 1
"""

print(build_order(dependencies))