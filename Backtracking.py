def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
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

def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
    #IF the candidate is a solution, that is, has all elements of the input data
    if set(candidate) == set(input_data):
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
    
print(sorted(permutations({1,2,3})))