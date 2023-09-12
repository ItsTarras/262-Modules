def shuffle(s, t):
    """Shuffles two strings and returns an overall string in that order"""
    if len(s) == 0:
        return t
    if len(t) == 0:
        return s
   
    #Recursion
    item = shuffle(s[1:], t)
    final_set = set()
    for string in item:
        pile = s[0] + string
        final_set.add(pile)
    
    second = shuffle(t[1:], s)
    for string in second:
        pile = t[0] + string
        final_set.add(pile)
    return final_set
    
print(sorted(shuffle('ab', 'cd')))