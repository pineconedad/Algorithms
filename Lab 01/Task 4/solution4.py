input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 4/input4.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 4/output4.txt', 'w')

n = int(input_file_object.readline())
print(n)

finalSchd= []
finalName = []
finalTime = []

for l in range(n):
    a =  input_file_object.readline()
    alist = a.split(" ")
    aname, atime = alist[0], alist[-1]
    finalSchd.append(a)
    finalName.append(aname)
    finalTime.append(atime)



def selectionSort (finalSchd, finalName, finalTime):
    for i in range(len(finalName)):
        min = i
        for j in range(i+1, n):
            if finalName[j] < finalName[min]:
                min = j
            elif finalName[j] == finalName[min]:
                if finalTime[j] > finalTime[min]:
                    min = j
        
        finalSchd[i], finalSchd[min] = finalSchd[min], finalSchd[i]
        finalTime[i], finalTime[min] = finalTime[min], finalTime[i]
        finalName[i], finalName[min] = finalName[min], finalName[i]

    return finalSchd, finalName, finalTime

schd, name, time = selectionSort(finalSchd, finalName, finalTime)

print(schd, name, time)

for p in range(n):
    out = schd[p]
    output_file_object.write(out)


output_file_object.close()


#took three separate lists to keep the schedule, name and time separately
#we applied selection sort, introduced a condition if the names are equal where the function compres between the departure time. Here min saves the target index of the train that depart late 
#we applied the sort in all three lists then added the schedule to the output file