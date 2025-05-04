def solve(grid):
    h = len(grid)
    w = len(grid[0])
    g = [row[:] for row in grid]
    d1 = {}
    d2 = {}
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                k1 = i - j
                k2 = i + j
                d1[k1] = d1.get(k1, 0) + 1
                d2[k2] = d2.get(k2, 0) + 1
    best1 = max(d1.items(), key=lambda x: x[1])
    best2 = max(d2.items(), key=lambda x: x[1])
    use1, key = (True, best1[0]) if best1[1] >= best2[1] else (False, best2[0])
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                if (use1 and i - j == key) or (not use1 and i + j == key):
                    g[i][j] = 8
    return g