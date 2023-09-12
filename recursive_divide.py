def recursive_divide(x, y):
    """divides the value as much as it can"""
    if x >= 0 and y > 0:
        return 1 + recursive_divide(x - y, y)
    return -1

print(recursive_divide(21, 3))