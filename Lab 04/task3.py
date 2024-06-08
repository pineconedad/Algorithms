inputt = open('input3.txt', 'r')
output = open('output3.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
for i in range(1, vert+1):
    adjlis[i] = []

for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), 1
    adjlis[elem].append(connect)
    adjlis[connect].append(elem)

def dfs(graph):
    color = {u: 'white' for u in graph}
    path = []
    for u in graph:
        if color[u] == 'white':
            dfs_visit(graph, u, color,path)

    return path

def dfs_visit(graph, u, color,path):

    color[u] = 'grey'
    path.append(u)

    for v in graph[u]:
        if color[v] == 'white':
            dfs_visit(graph, v, color,path)

    color[u] = 'black'


out = " ".join(list(map(str, dfs(adjlis))))
print(out)
output.write(out)
output.close()


# Adepth-first search (DFS) algorithm traverses the graph and collect vertices in a path. The DFS starts from each unvisited vertex and recursively explores all its adjacent vertices, marking them as visited in the process. It continues until all reachable vertices are visited. During the DFS traversal, vertices are colored white initially, then grey when visited but not yet fully explored, and finally black when fully explored. This coloring mechanism ensures that vertices are not revisited, preventing infinite loops.
# The DFS traversal collects vertices in a path list, which represents the order in which vertices are visited.