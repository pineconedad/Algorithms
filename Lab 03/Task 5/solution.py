inputt = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 5/input.txt', 'r')
outputt =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 5/output.txt', 'w')

l = int(inputt.readline())
arr = list(map(int, (inputt.readline().strip().split())))


def quickSort(A, p, r):
	if p < r:

		q = partition(A, p, r)

		quickSort(A, p, q - 1)

		quickSort(A, q + 1, r)

def partition(A, p, r):

	x = A[r]	#'x' is the pivot
	i = p - 1

	for j in range(p, r):
		if A[j] <= x:

			i = i + 1
			(A[i], A[j]) = (A[j], A[i])
			
	(A[i + 1], A[r]) = (A[r], A[i + 1])
	
	return i + 1


quickSort(arr, 0, l - 1)

out = " ".join(list(map(str, arr)))
outputt.write(out)
outputt.close()




# The partition function selects the last element of the array as the pivot (x) and rearranges the elements of the array such that all elements less than or equal to the pivot are on the left side, and all elements greater than the pivot are on the right side. It returns the index of the pivot after partitioning.
# The quickSort function recursively calls itself to sort the left and right subarrays around the pivot until the entire array is sorted.



