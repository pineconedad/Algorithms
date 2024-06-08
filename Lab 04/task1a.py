inputt = open('input1a.txt', 'r')
output =  open('output1a.txt', 'w')

fline = inputt.readline().strip().split(" ")

vert, edge = int(fline[0]), int(fline[1])

mat = [0]*(vert+1)

for i in range(len(mat)):
    mat[i] = [0]*(vert+1)


for j in range(edge):
    a = inputt.readline().strip().split(" ")
    elem, connect, wight = int(a[0]), int(a[1]), int(a[2])
    mat[elem][connect] = wight


for k in range(len(mat)):
    out = f'{" ".join(list(map(str, mat[k])))}\n'
    output.write(out)

output.close()


# It reads the first line of the input file, which contains two integers separated by a space: vert (number of vertices) and edge (number of edges).
# It initializes a square matrix mat of size (vert+1) x (vert+1) with all elements initially set to zero. This matrix represents the weights of connections between vertices.
# It iterates through each line in the input file, where each subsequent line contains three integers: elem (element), connect (connected element), and weight (weight of the connection).