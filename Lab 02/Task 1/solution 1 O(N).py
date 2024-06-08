input_file_object = open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 1/input1.1.txt', 'r')
output_file_object =  open('/Users/pineconedad/Academics/CSE221/Lab/22201704 Lab 02/Task 1/output1.txt', 'w')

integers =  input_file_object.readline().strip().split(" ")

n, s =  int(integers[0]), int(integers[1])
arr =  input_file_object.readline().strip().split(" ")



def sumgame2(arr):
    
    start, end = 0, len(arr)-1
    while start<end:
        sum = int(arr[start])+int(arr[end])
        if sum == s:
            return f"{start+1} {end+1}"
        else:
            if sum<s:
                start+=1
            else:
                end-=1
    
    return "IMPOSSIBLE"

out = sumgame2(arr)
output_file_object.write(out)

output_file_object.close()


#the funcftion uses two pointer, one at the start, one at the end 
#it traverses the whole array from both sides to find if the combination returns desired sum



