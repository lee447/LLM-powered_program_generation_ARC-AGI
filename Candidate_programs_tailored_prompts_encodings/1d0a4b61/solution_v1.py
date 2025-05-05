def solve(grid):
    n, m = len(grid), len(grid[0])
    rows_with_zero = [i for i in range(n) if any(grid[i][j] == 0 for j in range(m))]
    if not rows_with_zero:
        return [row[:] for row in grid]
    start, end = rows_with_zero[0], rows_with_zero[-1]
    top = [row[:] for row in grid[:start]]
    bottom = [row[:] for row in grid[end+1:]]
    H = end - start + 1
    res = [row[:] for row in grid]
    for k in range(H):
        if k < len(bottom):
            res[start + k] = bottom[k][:]
        else:
            idx = k - len(bottom)
            if idx < len(top):
                res[start + k] = top[idx][:]
            else:
                res[start + k] = top[-1][:]
    return res