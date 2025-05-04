def solve(grid):
    h, w = len(grid), len(grid[0])
    clr = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and c not in clr:
                mins = [i, j, i, j]
                for y in range(h):
                    for x in range(w):
                        if grid[y][x] == c:
                            mins[0] = min(mins[0], y)
                            mins[1] = min(mins[1], x)
                            mins[2] = max(mins[2], y)
                            mins[3] = max(mins[3], x)
                clr[c] = mins
    out = [[0]*w for _ in grid]
    items = sorted(clr.items(), key=lambda it: it[1][0])
    base_r = items[0][1][0]
    base_c = items[0][1][1]
    for c, (r0, c0, r1, c1) in items:
        dr = r0 - base_r
        dc = c0 - base_c
        for y in range(r0, r1+1):
            for x in range(c0, c1+1):
                if grid[y][x] == c:
                    out[y-dr][x-dc] = c
    return out