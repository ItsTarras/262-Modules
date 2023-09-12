def key_positions(seq, key):
    """Returns the sorted output of the algorithm"""
    count_array = []
    
    #Create a temporary sequence array to input lambda function
    temp_seq_array = []
    for item in seq:
        temp_seq_array.append(key(item))
    
    #print(temp_seq_array)
    #The maximum is that of where lambda has been applied to the element
    maximum = max(temp_seq_array)
    total = 0
    
    #print(f"The maximum is: {maximum}")
    #Creates a count array of length maximum item + 1
    for item in range(maximum + 1):
        count_array.append(0)
    #print(count_array)
    #Now check for each item and append it to the count list:
    for item in seq:
        count_array[key(item)] += 1
    #print(count_array)
    #Iterates through the counting array, and cumulatively adds them together.
    for index in range(0, maximum + 1):
        count_array[index], total = total, total+count_array[index] 
    return(count_array)

print(key_positions([1, -2, 0, 0, 3], lambda x: x)))