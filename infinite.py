def cycle_length(n):
    """Returns the number of processes for the famous 3x + 1 problem"""
    if n != 1:
        if n % 2 == 0:
            return 1 + cycle_length(int(n/2))
        else:
            return 1 + cycle_length((3*n) + 1)
    return 1
        
print(cycle_length(22))