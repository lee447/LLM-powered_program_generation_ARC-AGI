def solve(grid):
    r = len(grid)
    c = len(grid[0]) if r else 0
    cnt = 0
    for i in range(r-1):
        for j in range(c-1):
            if grid[i][j]==3 and grid[i][j+1]==3 and grid[i+1][j]==3 and grid[i+1][j+1]==3:
                cnt += 1
    if cnt > 3:
        cnt = 3
    out = [[0]*3 for _ in range(3)]
    for k in range(cnt):
        out[k][k] = 1
    return out