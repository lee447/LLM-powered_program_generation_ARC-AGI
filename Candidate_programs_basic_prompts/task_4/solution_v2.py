def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    limit = rows if rows < cols else cols
    orig = [i for i in range(limit) if grid[i][i] != 0]
    if len(orig) < 2:
        return [row[:] for row in grid]
    step = orig[1] - orig[0]
    new_val = max(grid[i][i] for i in orig) + 1
    out = [row[:] for row in grid]
    for r in range(orig[0], limit, step):
        if out[r][r] == 0:
            out[r][r] = new_val
    return out