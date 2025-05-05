def solve(grid):
    h = len(grid)
    w = len(grid[0])
    split = next(j for j in range(w) if all(grid[i][j] == 4 for i in range(h)))
    out = [[0]*4 for _ in range(h)]
    for i in range(h):
        cnt = 0
        for c in range(split):
            if grid[i][c] == 8 and (c == 0 or grid[i][c-1] != 8):
                if cnt < 2:
                    out[i][cnt] = 2
                cnt += 1
        cnt = 0
        for c in range(split+1, w):
            if grid[i][c] == 5 and (c == split+1 or grid[i][c-1] != 5):
                if cnt < 2:
                    out[i][2+cnt] = 2
                cnt += 1
    return out