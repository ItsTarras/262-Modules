def does_shuffling(s1, s2):
    if len(s1) == 1:
        return [s2[:i] + s1 + s2[i:] for i in range(len(s2) + 1)]
    if len(s2) == 1:
        return [s1[:i] + s2 + s1[i:] for i in range(len(s1) + 1)]
    return [s1[0]+ s for s in shuffle(s1[1:], s2)] + [s2[0] + s for s in shuffle(s1, s2[1:])]

def shuffle(s, t):
    if s == '' and t == '':
        return {''}
    result = does_shuffling(s, t)
    my_set = set()
    for item in result:
        my_set.add(item)
    return my_set

def shuffle_language(A, B):
    result = []
    if A == {''}:
        return list(B)
    if B == {''}:
        return list(A)
    for item1 in A:
        for item2 in B:
            result += list(shuffle(item1, item2))
    #Remove duplicates
    result = set(result)
    final = list(result)
    return final

print(sorted(shuffle_language({'ab'}, {'cd', 'e'})))
print(sorted(shuffle_language({}, {'aa', 'ab', 'bb'})))
print(sorted(shuffle_language({'ab', 'cd', 'ae'}, {})))
print(sorted(shuffle_language({}, {})))
print(sorted(shuffle_language({''}, {'ab', 'aa', 'ac'})))

print(sorted(shuffle_language({'aba', 'baa', 'aab'}, {'aab', 'bba', 'aaa'})) == ['aaaaab', 'aaaaba', 'aaaabb', 'aaabaa', 'aaabab', 'aaabba', 'aabaaa', 'aabaab', 'aababa', 'aabbaa', 'aabbab', 'aabbba', 'abaaaa', 'abaaab', 'abaaba', 'ababaa', 'ababab', 'ababba', 'abbaab', 'abbaba', 'abbbaa', 'baaaaa', 'baaaab', 'baaaba', 'baabaa', 'baabab', 'baabba', 'babaab', 'bababa', 'babbaa', 'bbaaab', 'bbaaba', 'bbabaa', 'bbbaaa'])