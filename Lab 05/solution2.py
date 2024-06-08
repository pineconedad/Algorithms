inputt = open('input2.txt', 'r')
output =  open('output2.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
for i in range(vert+1):
    adjlis[i] = []

for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), 1
    adjlis[elem].append(connect)

import heapq as hq

def topologicalSort(adj_lis):
    V = len(adj_lis.keys())
    in_degree = [0] * V

    for u in range(V):
        for x in adj_lis[u]:
            in_degree[x] += 1

    s = []
    for i in range(V):
        if in_degree[i] == 0:
            hq.heappush(s, i)

    cnt = 0
    top_order = []

    while s:

        u = hq.heappop(s)
        top_order.append(u)


        for x in adj_lis[u]:
            in_degree[x] -= 1
            if in_degree[x] == 0:
                hq.heappush(s, x)

        cnt += 1

    if cnt != V:
        return("IMPOSSIBLE")

    return " ".join(list(map(str, top_order[1::])))




out = topologicalSort(adjlis)
output.write(out)