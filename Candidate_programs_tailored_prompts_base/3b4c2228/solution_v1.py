def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    count = 0
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==3 and grid[i][j+1]==3 and grid[i+1][j]==3 and grid[i+1][j+1]==3:
                count += 1
    if count>3:
        count = 3
    output = [[0,0,0] for _ in range(3)]
    for k in range(count):
        output[k][k] = 1
    return output