def fib(n):
    """Uses fast doubling method to find the nth fibonacci number, time complexity of binary search"""
    f = [0, 1]
    binary_string = bin(n)[2:] 

    for item in binary_string:
        f2i1 = f[1]**2 + f[0]**2  
        f2i = f[0]*(2*f[1]-f[0]) 
        
        #Checks if the item is a 1 or 0, then 2i + 1 the first element, or 2i +1, 2i + 2
        if item == '0':
            f[0], f[1] = f2i, f2i1  # [F(2i), F(2i+1)]
        else:
            f[0], f[1] = f2i1, f2i1+f2i  # [F(2i+1), F(2i+2)]
 
    return f[0]

print(fib(7))