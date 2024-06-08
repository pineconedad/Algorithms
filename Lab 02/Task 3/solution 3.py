input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 3/input3.1.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 3/output3.txt', 'w')

n = int(input_file_object.readline())
start, end = [], []

for i in range(n):
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

manager1 = [start[0]]
manager2 = [end[0]]

for k in range (1,len(start)):
    if manager2[-1]<= start[k]:
        manager1.append(start[k])
        manager2.append(end[k])

cando = len(manager1)
output_file_object.write(f"{cando}\n")

for m in range(len(manager1)):
    out = f"{manager1[m]} {manager2[m]}\n"
    output_file_object.write(out)


output_file_object.close()


#sorted both the list of start time and end time using selection sort based on the end time 
#assigned task checking if the end time of the current task is lower or equal then the start time of the new task 
