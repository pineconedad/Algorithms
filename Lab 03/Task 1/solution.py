inputt = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 1/input.txt', 'r')
output =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 1/output.txt', 'w')

l = int(inputt.readline())
arr = list(map(int, (inputt.readline().strip().split())))

def merge(a, b):

    firstList = a  
    seconList = b

    firstLen = len(a)
    seconLen = len(b)
    
    newLis = []
    i = 0
    j = 0

    while i < firstLen and j < seconLen:
        if firstList[i] <= seconList[j]:
            newLis.append(firstList[i])
            i += 1
        else:
            newLis.append(seconList[j])
            j += 1
    while i < firstLen:
        newLis.append(firstList[i])
        i += 1
    while j < seconLen:
        newLis.append(seconList[j])
        j += 1

    return newLis

def mergesort(arra):

    if len (arra) <=1:
        return arra
    else:
        mid = len(arra)//2
        a1 =  mergesort(arra[:mid])
        a2 = mergesort(arra[mid:])
        return merge(a1, a2)
    
sorted = " ".join(list(map(str, mergesort(arr))))

output.write(sorted)
output.close()


#The merge function merges two sorted arrays
#mergesort recursively divides the array into halves until it reaches base cases of single elements, then merges them back together in sorted order.
#The merge function iterates through both lists simultaneously, comparing elements at corresponding indices. It appends the smaller element to a new list and advances the index of the list from which the element was taken. Once one of the lists is exhausted, it appends the remaining elements from the other list to the new list. 