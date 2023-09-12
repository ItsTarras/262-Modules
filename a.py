def foo(numbers): 
    result = [] 
    for i in range(len(numbers)): 
        sub = sorted(numbers[i:]) 
        result.append(sub[0])
    return result
    




print(foo([1, 2, 3, 3]))