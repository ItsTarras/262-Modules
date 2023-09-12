def epsilon_closure(node, array, my_set=set()):
    """recursively checks a node for its epsilon closures"""
    #print(array[node])
    #print(my_set)
    my_set.add(f"q{node}")
    node_list = array[node]
    if None in node_list:
        return set()
    else:
        for item in node_list:
            if int(item[1]) != node:
                item_num = int(item[1])
                #print(f"Node q{node} is connected to Node q{item_num}")
                epsilon_closure(item_num, array, my_set)
    return my_set
                
def zero_check(zero_array, epsilon_array, closure):
    #print(epsilon_array)
    zero = []
    for index in range(len(epsilon_array)):
        sorted_list = (sorted(list(epsilon_array[index])))
        #print(f"For the node: {epsilon_array[index]}")
        #Check where each member of the new epsilon array will go
        a_set = set()
        for node in sorted_list:
            #print(node)
            temp_list = []
            conversion = []
            index_node = int(node[1])
            for item in zero_array[index_node]:
                #print(index_node)
                if item != None:
                    next_node = int(item[1])
                    closing = epsilon_closure(next_node, closure, my_set=set())
                    #print(f"This is closing {closing}")
                    list_closing = list(closing)
                    for item in list_closing:
                        if item not in a_set:
                            a_set.add(item)
            if len(a_set) != 0 and node == sorted_list[-1]:
                #print(f"{sorted(list(epsilon_array[index]))} input 0 = {sorted(list(a_set))}")
                temp_list.append(sorted(list(a_set)))
        for item in temp_list:
            for items in item:
                conversion.append(items)
        if len(conversion) > 0:
            zero.append(conversion)
    return zero

def one_check(one_array, epsilon_array, closure):
    #print(epsilon_array)
    one = []
    for index in range(len(epsilon_array)):
        sorted_list = (sorted(list(epsilon_array[index])))
        #print(f"For the node: {epsilon_array[index]}")
        #Check where each member of the new epsilon array will go
        a_set = set()
        for node in sorted_list:
            #print(node)
            temp_list = []
            conversion = []
            index_node = int(node[1])
            for item in one_array[index_node]:
                #print(index_node)
                if item != None:
                    next_node = int(item[1])
                    closing = epsilon_closure(next_node, closure, my_set=set())
                    #print(f"This is closing {closing}")
                    list_closing = list(closing)
                    for item in list_closing:
                        if item not in a_set:
                            a_set.add(item)
            if len(a_set) != 0 and node == sorted_list[-1]:
                #print(f"{sorted(list(epsilon_array[index]))} input 1 = {sorted(list(a_set))}")
                temp_list.append(sorted(list(a_set)))
        for item in temp_list:
            for items in item:
                conversion.append(items)
        one.append(conversion)
    return one
                
def recursive_check(array):
    """Returns the set of epsilon closures"""
    empty = []
    for length in range(len(array)):
        empty.append(epsilon_closure(length, array, set()))
        
    #Now check if the item is a subset:
    for item in empty:
        index = 0
        while index < len(empty):
            #print(empty)
            if empty[index].issubset(item) and empty[index] != item:
                del empty[index]
            else:
                index += 1
    return empty


def convert(set_of_stuff, array=[]):
    """Converts set into list"""
    for item in set_of_stuff:
        array.append(list(item))  
    return array

def delete_duplicate_lists(inputs):
    """Deletes duplicate lists in linear time"""
    returnable = []
    for item in inputs:
        if sorted(item) not in returnable:
            returnable.append(sorted(item))
    return returnable
    
    
def main():
    #Add the closures in order of the nodes, in lists of lists, type None if empty.
    closure = ([['q3'], ['q2'], ['q2', 'q5'], [None], ['q3'], [None]])
    epsilon_array = (recursive_check(closure))
    #Add the list of lists in which input 0|1 will take you. Type None, if empty.
    zero_array = [['q1', 'q4'], [None], [None], [None], ['q1'], [None]]
    one_array = [[None], [None], [None], ['q0'], ['q2', 'q3'], ['q4']]
    
    epsilon = convert(epsilon_array)
    zero = zero_check(zero_array, epsilon_array, closure)
    one = one_check(one_array, epsilon_array, closure)
    #print("")
    #print(f"epsilon array = {epsilon_array} \n")
    #print(f"zero array = {zero} \n")
    #print(f"one array = {one} \n")
    
    all_nodes = delete_duplicate_lists(epsilon + zero + one)
    #for index in range(len(all_nodes)):
     #   print(f"{index + 1}: {all_nodes[index]}")
     
    #Hardcoded to check 10 iterations
    for number in range(10):
        all_ones = (one_check(one_array, all_nodes, closure))
        all_zeroes = (zero_check(zero_array, all_nodes, closure))
    
    

        for number in range(len(all_ones)):
            if all_ones[number] not in all_nodes:
                all_nodes.append(all_ones[number])
        for number in range(len(all_zeroes)):
            if all_zeroes[number] not in all_nodes:
                all_nodes.append(number) 
    
    #Prints all nodes possible from epsilon closure
    for item in range(len(all_nodes)):
        print(f"{item}: {all_nodes[item]}") 
        
        #Comment this out if it doesn't work when there's a dead state reachable
        #You will need to figure out on your own if it fails.
        print(f"input 1: {all_ones[item]}")
        #Comment this out if it doesn't work when there's a dead state reachable
        #You will need to figure out on your own if it fails.
        #print(f"input 0: {all_zeroes[item]}")
    
main()