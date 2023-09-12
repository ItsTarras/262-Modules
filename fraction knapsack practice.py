def fractional_knapsack(capacity, items):
    """Does shit"""
    values = []
    cost = 0
    for item in items:
        value = int(item[1]) / int(item[2])
        weight = int(item[2])
        temp = [value, weight]
        values.append(temp)
    
    values = sorted(values)
    values.reverse()
    print(values)
    for item in values:
        while item[1] > 0:
            if capacity > 0: 
                cost += item[0]
                item[1] -= 1
                capacity -= 1
            else:
                break
    print(values)
    return cost

# The example from the lecture notes
items = [
    ("Chocolate cookies", 12, 5),
    ("Potato chips", 9, 3),
    ("Pizza", 14, 5),
    ("Popcorn", 6, 2),
    ("item", 12, 4)]
print(fractional_knapsack(12, items))