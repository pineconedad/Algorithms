input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 2/input3.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 2/output.txt', 'w')


firstLen = int(input_file_object.readline())
firstList = input_file_object.readline().strip().split(" ")
seconLen = int(input_file_object.readline())
seconList = input_file_object.readline().strip().split(" ")
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
while i < firstLen:
    newLis.append(firstList[i])
    i += 1
while j < seconLen:
    newLis.append(seconList[j])
    j += 1

out = (" ".join(newLis))

output_file_object.write(out)
output_file_object.close()



#i and j variables re initialized to traverse list1 and list2
#first while loop compares the elements from two lists with the help of the variables i and j and adds the elements to the newLis
#every time an element is added to the newLis, the variable which is used to track the elements from which the element belongs is increased by 1
#rest of the elements is added using the last 2 while loops































# firstLen = int(input_file_object.readline())
# firstList = input_file_object.readline().strip().split(" ")
# seconLen = int(input_file_object.readline())
# seconList = input_file_object.readline().strip().split(" ")

# newLis = []

# if firstLen>=seconLen:
#     for i in range(seconLen):
#         if int(firstList[i])>=int(seconList[i]):
#             newLis.append(seconList[i])
#             newLis.append(firstList[i])
            
#         else:
#             newLis.append(firstList[i])
#             newLis.append(seconList[i])
            
        
#         print(newLis)


#     for j in range(firstLen-seconLen):
#         newLis.append(firstList[seconLen+j])

# else:
#     for i in range(firstLen):
#         if int(firstList[i])>=int(seconList[i]):            
#             newLis.append(seconList[i])
#             newLis.append(firstList[i])

#         else:
#             newLis.append(firstList[i])
#             newLis.append(seconList[i])
            

#     for j in range(seconLen-firstLen):
#         newLis.append(seconList[firstLen+j])


# print(newLis)
