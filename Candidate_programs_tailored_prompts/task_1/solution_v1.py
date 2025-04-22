def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            if (grid[i][j] == 3 and grid[i][j+1] == 3 and
                grid[i+1][j] == 3 and grid[i+1][j+1] == 3):
                count += 1
    output = [[0]*3 for _ in range(3)]
    for k in range(min(count, 3)):
        output[k][k] = 1
    return output