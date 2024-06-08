input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 1/input1.1.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 1/output1.txt', 'w')

integers =  input_file_object.readline().strip().split(" ")

n, s =  int(integers[0]), int(integers[1])
arr =  input_file_object.readline().strip().split(" ")

def sumgame(arr, n, s):
    for i in range(n):
        a =  int(arr[i])        

        for j in range(i+1,n):
            b = int(arr[j])
            if a+b == s:
                return f"{i+1} {j+1}"
    
    return "IMPOSSIBLE"

out = sumgame(arr, n, s)


output_file_object.write(out)

output_file_object.close()


#the sumgame function runs the main loop where it targets each element of the given array
#then for each targeted elemnet it runs another loop from the next index of the tagetted element and checks if the sum produces the required sum
#if it does it returns the 1 based index, if it does not it returns impossible
