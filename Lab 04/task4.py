inputt = open('input4.txt', 'r')
output = open('output4.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
for i in range(1, vert+1):
    adjlis[i] = []

for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), 1
    adjlis[elem].append(connect)


has_cycle = False

def dfs(graph):
    color = {u: 'white' for u in graph}

    for u in graph:
        if color[u] == 'white':
            dfs_visit(graph, u, color)


def dfs_visit(graph, u, color):

    global has_cycle
    color[u] = 'grey'

    for v in graph[u]:
        if color[v] == 'white':
            dfs_visit(graph, v, color)
        elif color[v] == 'grey':
            has_cycle = True

    color[u] = 'black'

out = dfs(adjlis)

if has_cycle == True:
    output.write("YES")
else:
    output.write("NO")

output.close()



#DFS is traversal is done. During traversal, it marks vertices as grey when they are visited but not fully explored, and black when they are fully explored. If a back edge is encountered during the DFS traversal (i.e., if a grey vertex is encountered), it indicates the presence of a cycle in the graph. The has_cycle variable is set to True in such cases. The has_cycle flag determines if there is a cycle in the graph or not.