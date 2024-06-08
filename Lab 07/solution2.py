inputt = open('input2.2.txt', 'r')
output = open('output2.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
for i in range(1, vert+1):
    adjlis[i] = []

for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), int(a[2])
    adjlis[elem].append((connect, wight))
    adjlis[connect].append((elem, wight))

import heapq


def prim_MST(graph, start):
    n = len(graph)
    key = [float('inf')] * (n + 1)  
    parent = [None] * (n + 1)  
    
    key[start] = 0 
    
    priority_queue = [(0, start)]  
    
    total_cost = 0 
    
    visited = set()  
    
    while priority_queue:
        current_key, u = heapq.heappop(priority_queue)  
        
        if u in visited:  
            continue
        
        visited.add(u)  
        
        total_cost += current_key  
        
        for v, weight in graph[u]:  
            if v not in visited and weight < key[v]:
                parent[v] = u 
                key[v] = weight  
                heapq.heappush(priority_queue, (key[v], v))  
    
    return total_cost

start_vertex = 1
minimum_spanning_tree = prim_MST(adjlis, start_vertex)
print(minimum_spanning_tree)


# prim_MST function, which implements Prim's algorithm for finding the minimum spanning tree of a graph. This function maintains a priority queue to efficiently select vertices with the smallest key values, ensuring that the algorithm traverses the graph in the most optimal manner. By iteratively selecting edges with the lowest weights, the function constructs the minimum spanning tree, ultimately returning the total weight of the tree.