def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    nonzero_rows = {i for i in range(h) if any(grid[i][j] != 0 for j in range(w))}
    nonzero_cols = {j for j in range(w) if any(grid[i][j] != 0 for i in range(h))}
    if not nonzero_rows or not nonzero_cols:
        return out
    fr, lr = min(nonzero_rows), max(nonzero_rows)
    fc, lc = min(nonzero_cols), max(nonzero_cols)
    for r in range(fr+1, lr):
        if all(grid[r][c] == 0 for c in range(w)):
            for c in range(w):
                out[r][c] = 2 if fc <= c <= lc else 1
    for c in range(fc+1, lc):
        if all(grid[r][c] == 0 for r in range(h)):
            for r in range(h):
                out[r][c] = 2 if fr <= r <= lr else 1
    return out