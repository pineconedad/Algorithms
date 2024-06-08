input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 1/input1b.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 1/output1b.txt', 'w')

n = int(input_file_object.readline())

for i in range(n):
  a = ((input_file_object.readline()).strip()).split(' ')
  x = int(a[1])
  y = int(a[3])

  b = str(a[1])+" " + str(a[2])+" " + str(a[3])

  if a[2] == '+':
    re = x+y
  elif a[2] == '-':
    re = x-y
  elif a[2] == '/':
    re = x/y
  elif a[2] == '*':
    re = x*y

  out = f"The result of {b} is {str(re)}\n"
  output_file_object.write(out)


output_file_object.close()



#'n' used to keep th track of no of test cases
#iteration is used to traverse from one test case to another
#test cases are 'stipped' to directly take the numbers and the operation signs provided
#'split' is used to get rid off the \n at the end of each line i the input file
