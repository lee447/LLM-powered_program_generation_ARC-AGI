def solve(grid):
    r, c = len(grid), len(grid[0])
    count = 0
    for i in range(r-1):
        for j in range(c-1):
            if grid[i][j] == 3 and grid[i][j+1] == 3 and grid[i+1][j] == 3 and grid[i+1][j+1] == 3:
                count += 1
    k = count if count <= 3 else 3
    out = [[0]*3 for _ in range(3)]
    for i in range(k):
        out[i][i] = 1
    return out