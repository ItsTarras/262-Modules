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


def is_strongly_connected(adj_list):
    """Checks if a graph is strongly connected"""
    #This assumes its possible to reach every node, no matter the starting node
    #print(adj_list)
    for item in adj_list:
        if item == []:
            return False
    directed_failed = False
    none_count = 0
    for index in range(len(adj_list)):
        none_count = 0
        array = bfs_tree(adj_list, index)
        #print(bfs_tree(adj_list, index))
        for item in array:
            if item == None:
                none_count += 1
                #print('+1')
            if none_count == 2:
                return False
    return True
    



graph_string = """\
D 3
0 1
1 0
0 2
"""

print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 3
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 4
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))

# Since we are passing an adjacency list to your algorithm,
# it will see an un directed graph as a directed one where each
# undirected edge appears as two directed edges.

graph_string = """\
U 5
2 4
3 1
0 4
2 1
"""

print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 6
0 1
1 2
2 0
3 4
4 5
5 3
2 4
"""

print(is_strongly_connected(adjacency_list(graph_string)))