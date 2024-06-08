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
    adjlis[connect].append(elem)


from collections import deque

def bfs(adj_list, source):
    
    Q = deque([source])
    d = {v: float('inf') for v in adj_list}
    d[source] = 0
    bfs_path = []
    
    
    while Q:
        u = Q.popleft()
        bfs_path.append(u)
        for v in adj_list[u]:
            if d[v] == float('inf'):
                d[v] = d[u] + 1
                Q.append(v)
    
    return bfs_path

out = " ".join(list(map(str, (bfs(adjlis, 1)))))
output.write(out)
output.close()


#The BFS algorithm starts by initializing a queue with the source vertex (vertex 1 in this case) and a dictionary to store the distances from the source vertex to all other vertices. It iteratively dequeues vertices from the queue and explores their neighbors. While dequeueing it adds the dequeued element to the 'bfs_pah' list which represents the path through which all the cities are explored.

# For each unvisited neighbor, it updates its distance from the source vertex and enqueues it for further exploration. This process continues until all reachable vertices are visited, ensuring that the distances stored in the dictionary represent the shortest paths from the source vertex to all other vertices in the graph.