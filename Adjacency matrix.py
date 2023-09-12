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


x = (adjacency_list(graph_string))


def adjacency_list(graph_str):
    """Takes textual string of graph and turns into list of lists"""
    iteration = 0
    directed = False
    weighted = False
    graph_list = []
    #print(graph_str)
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
                outer_list[vertex2].append((vertex1, None))
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
                outer_list[vertex2].append((vertex1, weight))
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

def reaching_vertices(adj_list, vertex):
    iterable = bfs_tree(adj_list, vertex)
    empty = []
    index = 0
    empty.append(vertex)
    while index < len(iterable):
        if iterable[index] != None:
            empty.append(index)
        index += 1
    return sorted(empty)


            
graph_string = """\
U 6
0 1
0 2
5 3
"""

adj_list = adjacency_list(graph_string)
for target in range(len(adj_list)):
    print(sorted(reaching_vertices(adj_list, target)))