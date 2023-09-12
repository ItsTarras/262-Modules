def sort(numbers, d):
    list_array = []
    for i in range(0,10):
        int_array = []#list for integer i
        list_array.append(int_array)

    for number in numbers:
        str_number = str(number)
        posval = 0
        if(len(str_number) >= d):
            posval = ord(str_number[-d]) - ord('0') 
            list_array[posval].append(number) 
        else:
            list_array[0].append(number)
    sortedList = [] 

    for int_array in list_array:
        for number in int_array:
            sortedList.append(number)

    return sortedList

def radix_sort(numbers, maxpos):
    finalList = numbers
    for d in range(1, maxpos+1):
        finalList = sort(finalList, d)

    return finalList


#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
#print(radix_sort([9, 57, 657], 2))