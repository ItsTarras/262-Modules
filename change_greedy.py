def change_greedy(amount, coinage):
    """Returns numbers of coins using a greedy algorithm"""
    sorted_coins = sorted(coinage)
    sorted_coins.reverse()
    returnable = []
    total = 0
    max_amount = amount
    #Sorted_coins is a sorted list with highest values first
    for item in sorted_coins:
        count = 0
        while max_amount - item >= 0:
            count += 1
            max_amount -= item
            total += item
        if count > 0:
            returnable.append((count, item))
        #print(returnable)
    #print(total)
    if total == amount:
        return returnable
    
    
print(change_greedy(82, [1, 10, 25, 5]))
print(change_greedy(80, [1, 10, 25]))
print(change_greedy(82, [10, 25, 5]))