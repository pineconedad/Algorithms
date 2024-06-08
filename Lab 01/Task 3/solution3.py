input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 3/input3.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 3/output3.txt', 'w')

n = int(input_file_object.readline())
arrID = (input_file_object.readline()).strip().split(' ')
arrMarks = (input_file_object.readline()).strip().split(' ')


def selectionSort (n, arrID, arrMarks):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if int(arrMarks[j]) < int(arrMarks[min]):
                min = j
        
        arrMarks[i], arrMarks[min] = arrMarks[min], arrMarks[i]
        arrID[i], arrID[min] = arrID[min], arrID[i]

    return arrID, arrMarks

id, marks = selectionSort(n, arrID, arrMarks)


for m in range(n):
    out = f"ID: {id[m]} Mark: {marks[m]}\n"
    output_file_object.write(out)


output_file_object.close()


#to keep the number of swapping operations minimum 'selection sort' is used. In each iteration, the code finds the minimum element’s index in the unsorted portion of the array and swaps it with the current index’s element. This gradually sorts the array from left to right.
#we compare based on the marks and apply the swapping operation both on the array of IDs and that of the marks of the respective students