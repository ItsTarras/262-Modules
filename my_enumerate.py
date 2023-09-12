def my_enumerate(items, i=0):
    """Returns a list of enumerated items using recursion"""
    new_list = []
    
    if i < len(items):
        new_list.append((i, items[i]))
        return new_list + my_enumerate(items, i + 1)
    
    return new_list


ans = my_enumerate([10, 20, 30])
print(ans)

ans = my_enumerate(['dog', 'pig', 'cow'])
print(ans)

ans = my_enumerate([])
print(ans)