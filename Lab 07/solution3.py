inputt = open('input3.txt', 'r')
output = open('output3.txt', 'w')

recof = int(inputt.readline().strip())


def rec_finder(n):
    step_lis = [1, 1]
    for i in range(2, n + 1):
        step_lis.append(step_lis[i - 1] + step_lis[i - 2])
    return step_lis[n]

recL = rec_finder(recof)
output.write(str(recL))
output.close()


# 'rec_finder' function calculates the nth Fibonacci number iteratively using dynamic programming. It initializes a list step_lis with the first two Fibonacci numbers, then iteratively calculates the subsequent Fibonacci numbers up to the given input n.