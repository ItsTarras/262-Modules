class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item({self.value},{self.weight})"


def knapsack(items, matrix, index, w):
    if matrix[index][w] >= 0:
        return matrix[index][w]

    if index == 0:
        q = 0
    elif items[index] is not None and items[index].weight <= w:
        q = max(knapsack(items, matrix, index - 1, w - items[index].weight) + items[index].value,
                knapsack(items, matrix, index - 1, w))
    else:
        q = knapsack(items, matrix, index - 1, w)
    matrix[index][w] = q
    return q


def max_value(items, weight):
    # None inserted to make 1 based indexing in array
    items.insert(0, None)
    n = len(items) - 1
    # created 2D array of rows = number of items
    # columns = capacity
    matrix = [[-1] * (weight + 1) for _ in range(n + 1)]
    return knapsack(items, matrix, n, weight)


def main():
    # The example from the lecture notes
    items = [
        Item(45, 3),
        Item(45, 3),
        Item(80, 4),
        Item(80, 5),
        Item(100, 8)]
    
    print(max_value(items, 10))   


    # Try a smallish problem with 10 different
    # random orderings.
    import random
    
    random.seed(12345)  # So everyone gets the same
    items = [Item(i, 10) for i in range(1, 11)]
    items.extend([Item(1, 5), Item(1, 4)])
    
    print(items)
    for i in range(10):
        random.shuffle(items)
        print(max_value(items, 99))
main()