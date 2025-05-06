def solve(grid):
    h = len(grid)
    w = len(grid[0])
    sep = next(j for j in range(w) if any(grid[i][j] == 4 for i in range(h)))
    size = min(sep, w - sep - 1)
    out = []
    for i in range(h):
        row = []
        for k in range(size):
            a = grid[i][k] == 8
            b = grid[i][sep + 1 + k] == 5
            row.append(2 if a ^ b else 0)
        out.append(row)
    return out