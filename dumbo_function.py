import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, i=0):
    """Takes a list of numbers and does weird stuff with it"""
    if len(data) == 0:
        return 0
    else:
        if i < len(data):
            if (data[i] // 100) % 3 != 0:
                return 1 + dumbo_func(data, i + 1)
            else:
                return dumbo_func(data, i + 1)
        else:
            return 0
        

"""import sys
sys.setrecursionlimit(100000)

def dumbo_func(data):
    #Takes a list of numbers and does weird stuff with it#
    if len(data) == 0:
        return 0
    else:
        if (data[0] // 100) % 3 != 0:
            return 1 + dumbo_func(data[1:])
        else:
            return dumbo_func(data[1:])"""

data = [677, 90, 785, 875, 7, 90393, 10707]
print(dumbo_func(data))        