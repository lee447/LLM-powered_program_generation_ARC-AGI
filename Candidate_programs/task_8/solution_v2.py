def solve(grid):
    R, C = len(grid), len(grid[0])
    cols = [c for c in range(C) if grid[-1][c] != 0]
    for c in cols:
        val = None
        for r in range(R-1, -1, -1):
            if grid[r][c] != 0:
                val = grid[r][c]
            elif val is not None:
                grid[r][c] = val
    return grid