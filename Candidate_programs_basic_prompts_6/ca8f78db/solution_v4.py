def solve(grid):
    h = len(grid)
    w = len(grid[0])
    pattern_row = None
    for row in grid:
        if 0 not in row and any(c > 1 for c in row):
            pattern_row = row
            break
    L = w
    for l in range(1, w+1):
        ok = True
        for i in range(w):
            if pattern_row[i] != pattern_row[i % l]:
                ok = False
                break
        if ok:
            L = l
            break
    pattern = pattern_row[:L]
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if res[i][j] == 0:
                res[i][j] = pattern[j % L]
    return res