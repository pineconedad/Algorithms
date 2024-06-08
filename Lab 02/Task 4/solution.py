input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 4/input.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 4/output.txt', 'w')

n = input_file_object.readline().strip().split(" ")
activ = int(n[0])
peop = int(n[1])
start, end = [], []

for i in range(activ):
    a = input_file_object.readline().split()
    start.append(int(a[0]))
    end.append(int(a[1]))


def selectionSort(array1, array2):
    size = len(array1)   
    for step in range(size):
        min_idx = step

        for j in range(step + 1, size):
            if array2[j] < array2[min_idx]:
                min_idx = j

        (array2[step], array2[min_idx]) = (array2[min_idx], array2[step])
        (array1[step], array1[min_idx]) = (array1[min_idx], array1[step])

selectionSort(start, end)
count = 0
busy = [-1]*peop

for k in range (0,len(start)):
    for p in range(peop):
        if busy[p] <= start[k]:
            busy[p] = end[k]
            count += 1
            break
        
        else:
            continue

output_file_object.write(str(count))
output_file_object.close()



#sorted using selection sort based on the end time of the tasks just like task 3
#after that created a list of length equal to the numer of available persons with each elements being -1 initially
#checked from the list if the person is free by checking if the start time of the task is greater or equal to the end time of the task the person is already doing
#if the person can do the task the element of the index of the person is updated with the end time of the task assigned to him