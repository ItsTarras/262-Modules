import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
    


#Create a matrix for the cache


def max_value(items, capacity):
    #Create the matrix
    matrix_sub, n = [None] * (capacity + 1), len(items)
    matrix = [matrix_sub] * (n + 1)

    
    #Cheekily create a new function that creates matrix and values instead of fors
    def values(items, value_list, n=0):
        if n < len(items):
            item = items[n]
            value_list.append(item.value)
            n += 1
            return values(items, value_list, n)
        else:
            return value_list
    
    values_list = (values(items, [], 0))
    #print(values_list, 'yes')

    
    def weights(items, weights_list, n=0):
        if n < len(items):
            item = items[n]
            weights_list.append(item.weight)
            n += 1
            return weights(items, weights_list, n)
        else:
            return weights_list
    
    weights_list = weights(items, [], 0)
    #print(weights_list)
                

    #print(capacity)
    #print(values)
    #print(weights)
    def knapsack(weights_list, values_list, capacity, n):
        """Recursively checks for values of items, and returns the best combo"""
        #Base cases
        if n == 0 or capacity == 0:
            return 0
        if matrix[n][capacity] is not None:
            return matrix[n][capacity]
        #print(matrix)
        
        
        #Diagram code
        #Checks if we are still going to be under capacity
        if weights_list[n - 1] <= capacity:
            #Newline cause the line is LOOOONG1!!
            #This will check the higher value of each branch
            matrix[n][capacity] = max(values_list[n - 1] +
                knapsack(weights_list, values_list, capacity-weights_list[n-1], n-1),
                knapsack(weights_list, values_list, capacity, n-1))
            #print('a')
            #print(matrix[n][capacity])
            return matrix[n][capacity]
        elif weights_list[n-1] > capacity:
            #Check the path prior
            matrix[n][capacity] = knapsack(weights_list, values_list, capacity, n-1)
            return matrix[n][capacity]
        
    
    return(knapsack(weights_list, values_list, capacity, n))

        
        




# The example from the lecture notes
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

print(max_value(items, 10))

# Try a smallish problem with 10 different
# random orderings.
import random

random.seed(12345)  # So everyone gets the same
items = [Item(i, 10) for i in range(1, 11)]
items.extend([Item(1, 5), Item(1, 4)])

print(items)

for i in range(10):
    random.shuffle(items)
    print(max_value(items, 99))