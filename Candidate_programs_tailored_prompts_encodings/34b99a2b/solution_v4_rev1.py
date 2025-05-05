def solve(grid):
    h = len(grid)
    w = len(grid[0])
    split = next(j for j in range(w) if all(grid[i][j] == 4 for i in range(h)))
    out = [[0]*4 for _ in range(h)]
    for i in range(h):
        cnt = 0
        c = 0
        while c < split:
            if grid[i][c] == 8:
                start = c
                while c < split and grid[i][c] == 8:
                    c += 1
                length = c - start
                n = (length + 1) // 2
                for _ in range(min(n, 2 - cnt)):
                    out[i][cnt] = 2
                    cnt += 1
            else:
                c += 1
        cnt = 0
        c = split + 1
        while c < w:
            if grid[i][c] == 5:
                start = c
                while c < w and grid[i][c] == 5:
                    c += 1
                length = c - start
                n = (length + 1) // 2
                for _ in range(min(n, 2 - cnt)):
                    out[i][2 + cnt] = 2
                    cnt += 1
            else:
                c += 1
    return out