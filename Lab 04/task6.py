inputt = open('input6.txt', 'r')
output =  open('output6.txt', 'w')

content = inputt.read().split("\n")

fline = content[0].strip().split(" ")
row, col = int(fline[0]), int(fline[1])

grid = [list(i) for i in content[1:row + 1]]



def dfs_diamfinder(grid, visited, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0
    
    visited[row][col] = True
    diamonds_collected = 0
    if grid[row][col] == 'D':
        diamonds_collected = 1
    
    diamonds_collected += dfs_diamfinder(grid, visited, row + 1, col)
    diamonds_collected += dfs_diamfinder(grid, visited, row - 1, col)
    diamonds_collected += dfs_diamfinder(grid, visited, row, col + 1)
    diamonds_collected += dfs_diamfinder(grid, visited, row, col - 1)
    
    return diamonds_collected

def max_diamonds(grid, row, col):
    rows, cols = row, col
    visited = [[False] * cols for _ in range(rows)]

    max_diamonds_collected = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '#':
                max_diamonds_collected = max(max_diamonds_collected, dfs_diamfinder(grid, visited, i, j))
    
    return max_diamonds_collected



output.write(str(max_diamonds(grid, row, col)))


# The dfs_diamfinder function recursively explores neighboring cells from a given starting position, counting the number of diamonds encountered while avoiding obstacles and previously visited cells. If a certain cell is not within the boundary or contains wall or already visited it returns 0. If not it initializes a variable to count the number of diamonds with 0 and then if the current cell contains a diamond updates the value to 1 and traverses in all 4 possible directions

# The max_diamonds function iterates over all cells in the grid, calling the DFS function from each valid cell to find the maximum number of diamonds that can be collected starting from that cell. Then compares the new received maximum number of diamonds collected from that position to the previous maximum number of diamonds that could be collected.