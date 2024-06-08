inputt = open('input1.2.txt', 'r')
output =  open('output1a.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
for i in range(1,vert+1):
    adjlis[i] = []

for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect = int(a[0]), int(a[1])

    adjlis[elem].append(connect)
  
has_cycle = False


def dfs(graph):
    color = {u: 'white' for u in graph}
    path = []
    for u in graph:
        if color[u] == 'white':
            dfs_visit(graph, u, color, path)

    return path


def dfs_visit(graph, u, color, path):

    global has_cycle
    color[u] = 'grey'
    path.append(u)

    for v in graph[u]:
        if color[v] == 'white':
            dfs_visit(graph, v, color, path)
        elif color[v] == 'grey':
            has_cycle = True

    color[u] = 'black'

out = " ".join(list(map(str, dfs(adjlis))))

if has_cycle == True:
    output.write("IMPOSSIBLE")
else:
    output.write(out)

inputt.close()
output.close()

