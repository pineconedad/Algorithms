inputt = open('input1b.txt', 'r')
output =  open('output1b.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

adjlis = {}
for i in range(vert+1):
    adjlis[i] = []


for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), int(a[2])
    adjlis[elem].append((connect, wight))

for k in range(vert+1):
    out = f'{k}: {" ".join(list(map(str, adjlis[k])))}\n'
    output.write(out)


output.close()


# It initializes an empty dictionary adjlis to store adjacency lists for each vertex. Each key in the dictionary represents a vertex, and the corresponding value is a list of tuples representing adjacent vertices and their weights.
# It iterates through integers from 0 to vert inclusive and initializes empty lists as values in the adjlis dictionary for each vertex.
# It iterates through each line in the input file, where each subsequent line contains three integers: elem (element), connect (connected element), and weight (weight of the connection).
# For each line, it appends a tuple (connect, weight) to the list corresponding to the key elem in the adjlis dictionary. This represents that there's a connection from elem to connect with the given weight.