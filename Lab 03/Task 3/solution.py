inputt = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 3/input.txt', 'r')
outputt =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 3/output.txt', 'w')

l = int(inputt.readline())
arr = list(map(int, (inputt.readline().strip().split())))
count = 0

def merge(a, b):

    global count

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
            count += firstLen-i
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
    
sortedd = mergesort(arr)
outputt.write(str(count))
outputt.close()


# The code initializes a variable count to keep track of the number of inversions.
# The merge function merges two sorted arrays while also counting the inversions. It compares elements from both arrays and when an element from the second array is less than an element from the first array, it adds the count of elements remaining in the first array to the inversion count.
# The mergesort function recursively divides the array into halves until it reaches the base case of arrays with one element. Then, it merges them back together while keeping track of the inversions.