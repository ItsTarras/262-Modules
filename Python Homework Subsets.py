def find(data, value):
    """Checks recursively for the first occurence of an item in a list"""

    if data == []:
        #print("that's the end")
        return None
    
    if data[0] == value:
        #print("I've been reached")
        return 0
    else:
        #print("im working")
        result = find(data[1:], value)
        if result == None:
            return None
        else:
            return result + 1



    
     
print(find(list(range(0,51)), 50))
print(find(["hi", "there", "you", "there"], "there"))
print(find([10, 20, 30], 0))