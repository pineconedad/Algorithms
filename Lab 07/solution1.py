inputt = open('input1.2.txt', 'r')
output = open('output1.txt', 'w')

fline = inputt.readline().strip().split(" ")

vill, connec = int(fline[0]), int(fline[1])

def find_par(x):
    if par[x] != x:
        par[x] = find_par(par[x]) 
    return par[x]


par = [0]*(vill+1)
child = [1]*(vill+1)

for i in range(len(par)):
    par[i] = i



for i in range(connec):
    nline = inputt.readline().strip().split(" ")

    u = find_par(int(nline[0]))
    v = find_par(int(nline[1]))

    if par[u]!=par[v]:
        par[u] = v
        # print(par[u], par[v])
        child[v] += child[u]
    output.write(str(f"{child[v]}\n"))


output.close()

# The par array is initialized to keep track of the parent nodes of each village in a disjoint set data structure. Initially, each village is its own parent, so par[i] is set to i.
# The child array is initialized to store the size of each village. Initially, each village is considered to have only itself, so child[i] is set to 1.
# The find_par(x) function is defined to find the parent node of a village x using path compression. This function recursively traverses the parent nodes until it reaches the root parent, while updating the parent of each visited node to directly point to the root parent. This helps in reducing the depth of the tree structure and hence the time complexity of future lookups.