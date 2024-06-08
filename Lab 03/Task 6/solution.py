inputt = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 6/input.txt', 'r')
outputt =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 6/output.txt', 'w')

l = int(inputt.readline())
arr = list(map(int, (inputt.readline().strip().split())))
q = int(inputt.readline())



def kfinder(A, p, r, k):
    if p < r:
        q = partition(A, p, r)
        if q == k - 1:
            return A[q]
        elif q > k - 1:            
            return kfinder(A, p, q - 1, k)
        elif q < k - 1:
            return kfinder(A, q + 1, r, k)
        
    return A[k - 1]  # to return the k-th element after the recursive calls

def partition(A, p, r):
    x = A[r]    # 'x' is the pivot
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r] = A[r], A[i + 1]
    
    return i + 1

for e in range(q):
    kth = int(inputt.readline())
    kthsmall = kfinder(arr, 0, l - 1, kth)
    outputt.write(f"{str(kthsmall)}\n")

outputt.close()


# The 'kfinder' function takes four parameters: the array A, the starting index p, the ending index r, and the value of k.
# It partitions the array around a pivot and checks if the pivot index is equal to k - 1. If so, it returns the element at that index.
# If the pivot index is greater than k - 1, it recursively searches the left subarray. If it's smaller, it recursively searches the right subarray.
# The partition function selects the last element of the array as the pivot and rearranges the elements of the array such that all elements less than or equal to the pivot are on the left side, and all elements greater than the pivot are on the right side. It returns the index of the pivot after partitioning.
# for loop iterates through the queries and finds the k-th smallest element for each query using the kfinder function.