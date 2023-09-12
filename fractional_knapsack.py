def fractional_knapsack(capacity, items):
    tuple_array = []
    total = 0
    for item in items:
        tuple_array.append((item[1]/item[2], item[2]))
    tuple_array = sorted(tuple_array)
    tuple_array.reverse()
    weight = 0
    #print(tuple_array)
    for item in tuple_array:
        maximum = item[1]
        #print(maximum)
        while maximum > 0:
            if weight < capacity:
                weight += 1
                maximum -= 1
                total += item[0]
            else:
                break
    return total

            
    print(total)
    
# The example from the lecture notes
items = [   
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))