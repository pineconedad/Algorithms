input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 1/input1a.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 01/Task 1/output1a.txt', 'w')

n = int(input_file_object.readline())

for i in range(n):
  a = int(input_file_object.readline())

  if a%2 == 0:
    text = f'{str(a)} is an even number\n'
  else:
    text = f'{str(a)} is an odd number\n'

  output_file_object.write(text)

output_file_object.close()


#'n' used to count the number of test cases
#iteration is done using 'for loops' for n times
#each iteration reads the number from input file as a string the performs operation on that after converting it to a integer