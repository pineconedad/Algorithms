inputt = open('input1.2.txt', 'r')
output =  open('output1b.txt', 'w')

fline = inputt.readline().strip().split(" ")

prereq_no, course_no = int(fline[0]), int(fline[1])

adjlis = {}
in_degree= [0] * (prereq_no+1)
for i in range(1, prereq_no+1):
    adjlis[i] = []

for j in range(course_no):
    a = inputt.readline().strip().split(" ")
    prereq, course = int(a[0]), int(a[1])
    adjlis[prereq].append(course)
    in_degree[course] += 1


from collections import deque

def bfs_courseorder(adj_list, in_degree):
    
    Q = deque()
    order = []
    N = len(adj_list.keys())

    for i in range(1, N+1):
        if in_degree[i] == 0:
            Q.append(i)
    
    
    while Q:
        u = Q.popleft()
        order.append(u)
        for v in adj_list[u]:
            in_degree[v] -= 1

            if in_degree[v] == 0:
                Q.append(v)
    
    return order


course_order = " ".join(list(map(str, bfs_courseorder(adjlis, in_degree))))

if len(course_order) < course_no:
    output.write("IMPOSSIBLE")
else:
    output.write(course_order)

