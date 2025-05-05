def solve(grid):
    n, m = len(grid), len(grid[0])
    hole_cols = set()
    for r in range(n):
        for c in range(1, m - 1):
            if grid[r][c] == 0 and grid[r][c - 1] != 0 and grid[r][c + 1] != 0:
                hole_cols.add(c)
    hole_cols = sorted(hole_cols)
    out = [row[:] for row in grid]
    for c in hole_cols:
        seg = [None] * n
        for r in range(n):
            if grid[r][c] != 0:
                seg[r] = grid[r][c]
            elif c > 0 and grid[r][c - 1] != 0:
                seg[r] = grid[r][c - 1]
            elif c + 1 < m and grid[r][c + 1] != 0:
                seg[r] = grid[r][c + 1]
        for i in range(n - 2, -1, -1):
            if seg[i] is None:
                seg[i] = seg[i + 1]
        for i in range(1, n):
            if seg[i] is None:
                seg[i] = seg[i - 1]
        for r in range(n):
            if grid[r][c] == 0 and seg[r] is not None:
                out[r][c] = seg[r]
    return out