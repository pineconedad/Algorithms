inputt = open('input3.txt', 'r')
output =  open('output3.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
adjlisTr = {}
for i in range(1,vert+1):
    adjlis[i] = []
    adjlisTr[i] = []

for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect = int(a[0]), int(a[1])
    adjlis[elem].append(connect)
    adjlisTr[connect].append(elem)

def dfs_finishtime(graph):
    color = {u: 'white' for u in graph}
    path = []
    for u in graph:
        if color[u] == 'white':
            dfs_visit_finishtime(graph, u, color, path)

    return path


def dfs_visit_finishtime(graph, u, color, path):

    color[u] = 'grey'
    for v in graph[u]:
        if color[v] == 'white':
            dfs_visit_finishtime(graph, v, color, path)

    
    color[u] = 'black'
    path.append(u)




def dfs(graph, finish):
    color = {u: 'white' for u in graph}
    
    for u in finish:
        if color[u] == 'white':
            path = []
            dfs_visit(graph, u, color, path)

            output.write(f'{" ".join(list(map(str, (path))))}\n')
     


def dfs_visit(graph, u, color, path):
    path.append(u)
    color[u] = 'grey'
    for v in graph[u]:
        if color[v] == 'white':
            dfs_visit(graph, v, color, path)

    
    color[u] = 'black'
    


finishtime = dfs_finishtime(adjlis)
finishtime.reverse()
dfs(adjlisTr, finishtime)


