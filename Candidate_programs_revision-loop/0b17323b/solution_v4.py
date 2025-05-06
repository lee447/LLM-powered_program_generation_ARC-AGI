def solve(grid):
    m = len(grid)
    n = len(grid[0]) if grid else 0
    size = min(m, n)
    out = [row[:] for row in grid]
    diag = [i for i in range(size) if grid[i][i] != 0]
    if len(diag) < 2:
        return out
    diffs = {}
    for i in range(1, len(diag)):
        d = diag[i] - diag[i - 1]
        diffs[d] = diffs.get(d, 0) + 1
    step = max(diffs, key=diffs.get)
    next_i = diag[-1] + step
    while next_i < size:
        out[next_i][next_i] = 2
        next_i += step
    return out