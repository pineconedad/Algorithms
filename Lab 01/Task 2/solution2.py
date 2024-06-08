input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 2/input2.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 2/output2.txt', 'w')

n = int(input_file_object.readline())

arr = input_file_object.readline().split(' ')

def bubbleSort(arr):
  issorted = True
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if int(arr[j]) > int(arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        issorted = False

    if issorted == True:
      return arr

  return arr

text = (bubbleSort(arr))
out = ' '.join(text)
output_file_object.write(out)




output_file_object.close()



#'arr' takes the array/list provided to be sorted
#we introduce a flag in the bubbleSort function which is changed under the scope of nested loop if any elements are swapped
#under the scope of first loop if the flag remains unchanged, we beak the loop hence in the best case scenario time complexity becomes Θ(n)