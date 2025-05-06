def solve(grid):
    h = []
    R, C = len(grid), len(grid[0])
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 5:
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 0:
                        h.append((ni, nj))
    h1, h2 = sorted(h)
    r1, c1 = h1; r2, c2 = h2
    res = [row[:] for row in grid]
    if c1 <= c2:
        for i in range(r1+1, r2):
            for j in range(c1, c2):
                if res[i][j] == 0:
                    res[i][j] = 4
        if res[r1][c1] == 0:
            res[r1][c1] = 4
        if res[r2][c2] == 0:
            res[r2][c2] = 4
        for j in range(c1, c2+1):
            if res[r2][j] == 0:
                res[r2][j] = 4
    else:
        for i in range(r1+1, r2):
            for j in range(c2, c1+1):
                if res[i][j] == 0:
                    res[i][j] = 4
        if res[r1][c1] == 0:
            res[r1][c1] = 4
        if res[r2][c2] == 0:
            res[r2][c2] = 4
        for j in range(c2, c1+1):
            if res[r1][j] == 0:
                res[r1][j] = 4
    return res