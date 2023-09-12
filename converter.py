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


def format_sequence(converters_info, source_format, destination_format):
    """info is graph, source is starting vertex, destination is final"""
    empty_answer = []
    if destination_format == source_format:
        return [source_format]
    start = source_format
    end = destination_format
    lists = adjacency_list(converters_info)
    parent = bfs_tree(lists, source_format)
    destination_update = destination_format
    
    #print(parent)
    #Parent is an array of the parents. Find the parent of the destination, and climb up.
    print(parent)
    print(f"The destination is {destination_update}")
    
    if parent[destination_update] != None:
        while parent[destination_update] != None:
            empty_answer = [(parent[destination_update])] + empty_answer
            print(empty_answer)
            item = destination_update
            destination_update = parent[destination_update]
            print(f"Node {item}'s parent is {destination_update}")
        empty_answer.append(destination_format)
        print(f"The starting node has been reached, since its parent is 'none'")
        return empty_answer
    else:
        return "No solution!"
        

converters_info_str = """\
D 5
0 1
0 2
1 2
2 3
1 3
3 0
"""

source_format = 1
destination_format = 0

print(format_sequence(converters_info_str, source_format, destination_format))

