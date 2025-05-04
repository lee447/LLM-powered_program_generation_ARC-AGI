def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = 0
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == 3 and grid[i][j+1] == 3 and grid[i+1][j] == 3 and grid[i+1][j+1] == 3:
                cnt += 1
    if cnt > 3: cnt = 3
    res = [[0,0,0] for _ in range(3)]
    for k in range(cnt):
        res[k][k] = 1
    return res