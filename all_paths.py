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

def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack((source, ), input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


def add_to_output(candidate, output_data):
    output_data.append(candidate)


def should_prune(candidate):
    return False

def is_solution(candidate, destination):
    """Returns True if the candidate is complete solution"""
    #IF the candidate is a solution, that is, has all elements of the input data
    if candidate == destination:
        return True
    else:
        return False


def children(candidate, input_data):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    #Create a list for all children
    child = []
    
    #Iterate through input data and check if the item is not a child
    #Issue 1: RECURSION SUCKS
    for item in input_data:
        
        #Goes through input_data
        if item not in candidate:
            #appends a tuple with the candidate, + the current item.
            child.append(candidate + (item, ))
    return child