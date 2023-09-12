def change(value, coinage):
    """Nested function"""
    returnable = []

    #Cacheing to stop timeouts
    cache = dict()

    def recursive_change(value, coinage, current_result = []):
        lists = []
        for item in coinage:
            lists.append([item[0], item[1]])
            
        if value in cache.keys():
            return []+cache[value] 

        # base case
        if value == 0:
            return []

        if value < 0: 
            return [-90]

        best_combo = [-1]

        for coin in lists:
            remains = coin[1]
            print(coin)
            if coin[1] > 0:
                coin[1] -= 1
                current_result = recursive_change(value - coin[0], lists)
            coin[1] = remains
            if current_result == [] or current_result[0] >= 0: 
                current_result.append(coin)
                if best_combo[0] < 0:
                    best_combo = current_result 
                else:
                    if len(current_result) < len(best_combo):
                        best_combo = current_result

        cache[value]=[]+best_combo
        #dictionary = { best: best_combo.count(best) for best in best_combo}
        return best_combo

    #Calls function, checks number of items, and turns it into list of tuples.
    final_combo = (recursive_change(value, coinage))
    listable = sorted(list(set(final_combo)))
    listable.reverse()
    for item in listable:
        returnable.append((item, final_combo.count(item)))
    return returnable

change(32, [(1, 9), (10, 2), (25, 3)])