inputt = open('input1ii.txt', 'r')
output =  open('output1.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
for i in range(1, vert+1):
    adjlis[i] = []


for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), int(a[2])
    adjlis[elem].append((connect, wight))

given_source = int(inputt.readline())

import heapq

def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    parents = {vertex: None for vertex in graph}

    distances[source] = 0

    pq =  [(distances[source], source)]

    while pq:
        cost, current = heapq.heappop(pq)

        if cost > distances[current]:
            continue

        for neighbor, weight in graph[current]:
            new_path = cost + weight

            if distances[neighbor] > new_path:
                distances[neighbor] = new_path
                parents[neighbor] = current
                heapq.heappush(pq, (distances[neighbor], neighbor))

    
    return distances, parents


sssp, sssp_parents = dijkstra(adjlis, given_source)

print(sssp, sssp_parents)
for i in sssp:
    if sssp[i] == float("inf"):
        sssp[i] = -1


out = " ".join(list(map(str, list(sssp.values()))))
output.write(out)
output.close()

# Dijkstra's algorithm for finding the shortest paths from a given source vertex to all other vertices in a weighted graph. The algorithm maintains a priority queue (heap) to efficiently select the vertex with the minimum distance at each step. For each neighboring node of the extracted node: Calculates the distance to the neighboring node through the extracted node; if this distance is smaller than the current known distance to the neighboring node, updates the distance; adds the neighboring node to the priority queue with its updated distance. After computing the shortest paths, replacing infinity values denoting unreachables nodes are replaced with -1.
