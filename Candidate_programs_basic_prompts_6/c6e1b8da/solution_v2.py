def solve(grid):
    H, W = len(grid), len(grid[0])
    r = next(i for i,row in enumerate(grid) if all(v==0 for v in row))
    c = next(j for j in range(W) if all(grid[i][j]==0 for i in range(H)))
    res = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v!=0:
                di, dj = i-r, j-c
                ni, nj = r + dj, c - di
                res[ni][nj] = v
    return res