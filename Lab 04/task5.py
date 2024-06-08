inputt = open('input5.txt', 'r')
output =  open('output5.txt', 'w')


fline = inputt.readline().strip().split(" ")

vert, edge, dest = int(fline[0]), int(fline[1]), int(fline[2])

adjlis = {}
for i in range(1, vert+1):
    adjlis[i] = []

for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), 1
    adjlis[elem].append(connect)
    adjlis[connect].append(elem)


from collections import deque

def shortest_traversal_bfs(adj_list, source=1):
    
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
    
    return bfs_path, d


path, time = shortest_traversal_bfs(adjlis)

shortest_path = [dest]
loc_level = time[dest]

while shortest_path[-1] != 1:
    loc = shortest_path[-1]

    for l in adjlis[loc]:
        if time[l] == loc_level -1:
            shortest_path.append(l)
            loc_level-=1
            break

shortest_path.reverse()
out1 = time[dest]
out2 = " ".join(list(map(str, shortest_path)))

out = f"Time: {out1} \nShortest Path: {out2}"
output.write(out)



#BFS is applied to find the shortest traversal path from the source vertex (vertex 1 by default) to all other vertices in the graph. IThe BFS algorithm starts by initializing a queue with the source vertex (vertex 1 in this case) and a dictionary to store the distances from the source vertex to all other vertices. It iteratively dequeues vertices from the queue and explores their neighbors. For each unvisited neighbor, it updates its distance from the source vertex and enqueues it for further exploration. This process continues until all reachable vertices are visited, ensuring that the distances stored in the dictionary represent the shortest paths from the source vertex to all other vertices in the graph.

#After obtaining the shortest traversal times, the code backtracks from the destination vertex to reconstruct the shortest path by following vertices with decreasing traversal times until it reaches the source vertex. The backtracking process starts from the destination vertex and iterates over its adjacent vertices. It selects the vertex with a traversal time one less than the current level, indicating a closer proximity to the source vertex. This vertex is appended to the shortest path, and the process continues iteratively until reaching the source vertex. This ensures that the reconstructed path reflects the shortest traversal path from the source to the destination vertex.