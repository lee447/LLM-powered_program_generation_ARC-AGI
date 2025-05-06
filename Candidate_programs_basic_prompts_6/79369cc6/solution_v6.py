def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    dirs = [(-1,1),(0,1),(1,0),(1,-1),(0,-1),(-1,0)]
    for i in range(1, h-1):
        for j in range(1, w-1):
            if out[i][j] != 4:
                cnt = 0
                for di,dj in [( -1,1),(1,-1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < h and 0 <= nj < w and out[ni][nj] != 0 and out[ni][nj] != 4:
                        cnt += 1
                if cnt == 2:
                    out[i][j] = 4
    for i in range(h-1):
        for j in range(w-1):
            if out[i][j] != 4 and out[i][j+1] != 4 and out[i+1][j] != 4 and out[i+1][j+1] != 4:
                s = {out[i][j], out[i][j+1], out[i+1][j], out[i+1][j+1]}
                if len(s) == 4:
                    out[i+1][j] = 4
    return out