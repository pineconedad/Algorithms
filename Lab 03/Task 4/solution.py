inputt = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 4/input.txt', 'r')
outputt =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 03/Task 4/output.txt', 'w')

l = int(inputt.readline())
arrad = list(map(int, (inputt.readline().strip().split())))


def getabsMax(a, b):

    if abs(a[0])>abs(b[0]):
        return a
    
    else: 
        return b

    
def getMax(c, d):

    if c[0]>d[0]:
        return c
    else:
        return d
    
def divi(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        L = divi(arr[:mid])
        R = divi(arr[mid:])
        return getabsMax(L, R)
    
def divi2(arra):
    if len(arra)<=1:
        return arra
    else:
        mid = len(arra)//2
        L = divi(arra[:mid])
        R = divi(arra[mid:])
        return getMax(L, R)
    
absMax = divi(arrad)[0]

for i in range (l):
    if arrad[i] == absMax:
        idx = i

secMax = divi2(arrad[:idx])[0]

outputt.write(str(secMax + absMax**2))
outputt.close()


# getabsMax(a, b): Compares the absolute values of two sub arrays and returns the one with the higher absolute value.
# getMax(c, d): Compares the values of two sub arrays and returns the one with the higher value.
# divi(arr): Divides the array into halves recursively and finds the tuple with the maximum absolute value.
# divi2(arra): Divides the array into halves recursively and finds the tuple with the maximum value.
# It finds the maximum absolute value absMax by calling divi(arrad)[0].
# It then finds the index of the maximum absolute value absMax in the original array.
# It finds the second maximum value secMax by calling divi2(arrad[:idx])[0], which finds the maximum value in the subarray before the maximum value.