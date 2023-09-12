def elements(list1, list2):
    concatenations = []
    for item in list1:
        #if item not in concatenations:
            #concatenations.append(item)
        for item2 in list2:
            #if item2 not in concatenations:
                #concatenations.append(item2)
            print(item, item2)
            if len(item + item2) > 0:
                if item[-1] == item2[0]:
                    if len(item) > 0 and len(item2) > 0:
                        string = item[0:-1] + item2
                    #print(f"{item}, {item2}")
                if (string) not in concatenations:
                    concatenations.append(string)
    print(len(concatenations))
    return sorted(concatenations)

def length_checker(elements):
    """Checks how many strings of length are less"""
    length_list = []
    for item in elements:
        if item not in length_list:
            length_list.append(item)
        for item2 in elements:
            product2 = item + item2
            if product2 not in length_list:
                length_list.append(product2)
            for item3 in elements:
                product3 = product2 + item3
                if product3 not in length_list:
                    length_list.append(product3)
    print(len(sorted(length_list)))
    return (sorted(length_list))


def all_strings(alpha,length):
    new_list=[]
    if length > 0:
        lst = all_strings(alpha, length - 1)
        for string in lst:
            for ch in alpha:
                new_list.append(str(string)+str(ch))

        if len(lst)==0:
            for ch in alpha:
                new_list.append(str(ch))
                        
        return new_list 
    else:
        new_list.append('')
        return new_list
    
print(elements(['a','bd','ca','cab','d','dbb'],['a','aa','ab','bda','bdb','c']))

def fusion(s, t):

    result = []

    for a in s:
        for b in t:

            if (a[-1] == b[0]):
                result.append(a+b[1:])

    return result


L1 = ['a','ca','cbb','d','dbb','dd']
L2 = ['a','ac','ad','baa','bda','c']
print(len(fusion(L1, L2)))