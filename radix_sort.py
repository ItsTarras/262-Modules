def radix_sort(numbers, d):
    final_ints = []
    strings = []
    for i in numbers:
        strings.append(str(i))  
    ds = list(range(1,d+1))
    ds.sort()
    while len(ds) > 0:
        d = ds[0]
        final_list = []
        while len(strings) > 0:
            low = strings[0]
            for i in range(0,len(strings)):
                if len(strings[i]) <= -d:
                    low = strings[i]
                else:
                    if strings[i][-d] < low[-d]:
                        low = strings[i]
            final_list.append(low)
            strings.remove(low)
        ds.pop(0)
        strings = final_list
        #print(strings)
    for i in final_list:
        final_ints.append(int(i))  
    return final_ints

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))


print(radix_sort([9, 57, 657], 2))