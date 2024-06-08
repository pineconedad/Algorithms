input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 2/input3.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 2/output.txt', 'w')


firstLen = int(input_file_object.readline())
firstList = (list(map(int, input_file_object.readline().strip().split(" "))))
seconLen = int(input_file_object.readline())
seconList = (list(map(int, input_file_object.readline().strip().split(" "))))

a = firstList + seconList


newLis = sorted(a) 

out = " ".join(str(i) for i in newLis)

output_file_object.write(out)
output_file_object.close


#both the list extracts the arrays from the input file and converts the strings into integers
#both the lists are concatenated and then sorted using the sorted function