inputt = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 2/input1.txt', 'r')
outputt =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 2/output.txt', 'w')

n = int(inputt.readline())
arr =  list(map(int, (inputt.readline().strip().split(" "))))

def maxfind (arra):
    size = len(arra)
    mid = size//2
    if size>1:
        left = maxfind(arra[0:mid])
        right = maxfind(arra[mid:])
        if (left)>(right):
            return left 
        else:
            return right
    else:
        return (arra[0]) 
        
out = maxfind(arr)

outputt.write(str(out))
outputt.close()

# The maxfind function recursively finds the maximum integer in the array.
# It divides the array into halves until it reaches individual elements, then compares and returns the maximum of the left and right halves.